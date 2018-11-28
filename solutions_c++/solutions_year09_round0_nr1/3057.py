#include<iostream>
using namespace std;

int main()
{
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	string arr[D];
	for(int i=0;i<D;i++)
	{
		cin>>arr[i];
	}
	for(int i=0;i<N;i++)
	{
		string patt;
		cin>>patt;
		int sum=0;
		for(int j=0;j<D;j++)
		{
			string test=arr[j];
			int ind=0;
			int choice=0;
			int out=1;
			for(int k=0;k<patt.length();k++)
			{
			//	cout<<test<<"plzz"<<test[ind]<<"iii"<<patt[k]<<endl;
			//	cout<<test<<endl;
				if(patt[k]=='(')
					choice=1;
				if(patt[k]==')')
				{
					//cout<<"rejected"<<test<<endl;
					out=0;
					break;
				}
				if(choice==0&&patt[k]!='('&&patt[k]!=')')
				{
					if(patt[k]!=test.at(ind)){
						//cout<<"hre??"<<endl;
						out=0;
						break;
					}
					else{
						//cout<<"mmm"<<endl;
						ind++;
					}
				}
				if(choice==1&&patt[k]!='('&&patt[k]!=')')
				{
					if(patt[k]==test.at(ind)){
						k=patt.find(")",k);
						choice=0;
						ind++;
					}
				}
			}//out of for loop
			if(out==1)
				sum+=1;
		}
			cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}

}		


