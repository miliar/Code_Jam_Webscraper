#include<iostream>
using namespace std;
int powerOfTen(int d)
{
	int p=1;
	while(d--)
	p=p*10;
	return p;
}

int digitCount(int num)
{
   int count=0;
   while(num>0)
   {
   	count++;
    	num/=10;	
	}
	return count;
}

int main()
{
	int t;
	cin>>t;
	int k=0,A,B;
	
	while(k<t)
	{  
 		cin>>A>>B;
      int pairCount=0;
      int flag[2000001]={0};
 		for(int num=A;num<=B;num++)
		{
		    if(flag[num]==1)continue;
   	   int rot = digitCount(num);
   		int copyNum = num;
         int copyRot=rot;
         int count=1;
         while(rot--)
			{
   	      int r = copyNum%powerOfTen(rot);
            if(digitCount(r)<rot)
            	continue;
            int newNum = (copyNum/powerOfTen(rot)) +r*powerOfTen(copyRot-rot);
            if(newNum>num && newNum<=B && flag[newNum]==0)  			
			   {	
					flag[newNum]=1;count++;
			        //		cout<<num<<","<<newNum<<endl;
			   }	    																			
			}
			pairCount += (count*(count-1))/2; 
		}
      cout<<"Case #"<<++k<<": "<<pairCount<<endl; 	
	}
	return 0;
}
