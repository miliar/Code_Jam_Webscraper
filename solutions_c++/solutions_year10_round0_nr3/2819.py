
#include<stdio.h>

int main(void){
	long int test;
	long int nride;
	long int np;
	long int ngroup;
	long int glist[1001];
	long int intglist[1001];
	long int money;
	long int period;
	long int periodmoney;
	long int tmp;
	int ti;
	int i;
	int mark;
	int markend;
	scanf(" %ld",&test);
    // printf("%ld\n",test);
	for(ti=0;ti<test;ti++){
        scanf(" %ld",&nride);
        // printf("%ld %ld %ld\n",nride,np,ngroup);
        scanf(" %ld",&np);
        // printf("%ld %ld %ld\n",nride,np,ngroup);
        scanf(" %ld",&ngroup);
        // printf("%ld %ld %ld\n",nride,np,ngroup);
        for(i=0;i<ngroup;i++)scanf("%ld",glist+i);

        // intglist[0]=glist[0];
        // for(i=1;i<ngroup;i++)intglist[i]=intglist[i-1]+intglist[i];

        mark=0; // can ride
        markend=ngroup-1; // can ride
        period=0;
        periodmoney=0;
        money=0;
        for(i=0;i<nride;i++){
			tmp=0;
            // speedup
            if(i!=0&&period!=0&&nride>i+period-1){
                i=i+period-1;
                money+=periodmoney;
                continue;
            }

            while(1){
                if((mark!=markend)&&(tmp+glist[mark]<=np)){
					// not last person
                    tmp+=glist[mark];
                    mark=(mark+1)%ngroup;
                }
                else if(mark!=markend){
                    // too many people
                    // go
                    markend=(mark-1+ngroup)%ngroup;
                    money+=tmp;
                    if(period==0&&mark==0&&markend==ngroup-1){
                        period=i+1;
                        periodmoney=money;
                    }
					break;
                }
				else if((mark==markend)&&(tmp+glist[mark]<=np)){
					// the last group
					// go
					tmp+=glist[mark];
					markend=mark;
					mark=(mark+1)%ngroup;
					money+=tmp;
					if(period==0&&mark==0&&markend==ngroup-1){
						period=i+1;
						periodmoney=money;
					}
					break;
				}
				else if(mark==markend){
					// the last group is too big
					// go
					markend=(mark-1+ngroup)%ngroup;
					money+=tmp;
					if(period==0&&mark==0&&markend==ngroup-1){
						period=i+1;
						periodmoney=money;
					}
					break;
				}
            }
        }
        printf("Case #%d: %ld\n",ti+1,money);
	}
	return 0;
}
