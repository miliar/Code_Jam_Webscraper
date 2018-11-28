#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	freopen("prb1.txt","r",stdin);
	freopen("ans1.txt","w",stdout);
	int casen,no;

	cin>>no;

	for(casen=1;casen<=no;casen++)
	{
                                  char num[22];
                                  int len=0,k=0;
                                  len=0;
                                  cin>>num;
                                  while(num[len]!='\0')
                                  len++;
                                  
                                  for(k=len;k>=0;k--)
                                  num[k+1]=num[k];
                                  
                                  num[0]='0';
                                  
                                  
                                  next_permutation(num,num+len+1);

        if(num[0]!='0')
		cout<<"Case #"<<casen<<": "<<num<<endl;
		else
		{
		cout<<"Case #"<<casen<<": ";
		for(k=1;k<=len;k++)
		cout<<num[k];
		
		cout<<endl;
        }
	}


}
