#include <stdio.h>
typedef unsigned long num_t;

num_t moneyMade(num_t noOfRides,num_t noOfGroups,num_t*groups,num_t maxCap){
	num_t queueHead=0,bucks=0,load=0,isfirst=1,queueEnd,isFullLoad=0;
	num_t grouporder[1000],bucksmade[1000],curIndex;
	for(int i=0;i<1000;i++)
		grouporder[i]= -1;
	printf("noofrides= %lu maxcap= %lu\n",noOfRides,maxCap);
	for(num_t i=0;i<noOfRides;i++)
	{
		load=0;
		queueEnd= (queueHead+noOfGroups-1)%noOfGroups;
		for(int j=0;j<1000;j++)
			if(grouporder[j]==-1){
				grouporder[j]= queueHead;
				curIndex= j;
				break;
			}
			else if(grouporder[j]==queueHead){
				//found a repeating sequence
				//find sum and return
				int noOfTransitions=0;
				num_t tempBucks=0;
				for(int k=j;k<1000;k++){
					if(grouporder[k]!=-1)
					{
						noOfTransitions++;
						tempBucks+= bucksmade[k];
					}
					else
						break;
				}
				i= noOfRides-i;
				//i more rides remaining
				bucks+= (i/noOfTransitions)*tempBucks;
				for(int k=j;k - j <i%noOfTransitions;k++)
					bucks+= bucksmade[k];
				return bucks;
			}
		while(1){
			if(load+groups[queueHead]<=maxCap){
				printf("%d ",groups[queueHead]);
				load+= groups[queueHead];
				if(queueHead==queueEnd){
					printf(" full ");
					isFullLoad=1;
					break;
				}
				queueHead= (queueHead+1)%noOfGroups;
			}
			else
				break;
		}
		if(load==0)
			return 0;
		else if(isFullLoad!=0)
			return load*noOfRides;
		else{
				bucks+= load;
				bucksmade[curIndex]= load;
		}
		printf("\n%lu$ @ %lu ppl\n",bucks,load);
	}
	return bucks;
}

int main()
{
	FILE*fp= fopen("input.txt","r");
	if(fp){
		num_t lines;
		num_t noOfRides, noOfGroups, groups[1000], maxCap;
		fscanf(fp,"%lu",&lines);
		printf("%lu times\n",lines);
		for(num_t i=0;i<lines;i++)
		{
			fscanf(fp,"%lu %lu %lu",&noOfRides,&maxCap,&noOfGroups);
			for(num_t j=0;j<noOfGroups;j++)
				fscanf(fp,"%lu",&groups[j]);
			printf("\nCase #%lu: %lu\n",i+1,moneyMade(noOfRides,noOfGroups,groups,maxCap));
		}
	}
	else
		printf("Error opening file\n");
	return 0;
}