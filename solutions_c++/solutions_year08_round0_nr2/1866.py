#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
int as[201];
int val(string a)
{
	bool flag=false;
	int i,x=0,y=0;
	for(i=0;i<a.size();i++)
	{
		if(a[i]==':')	
		{flag=true;continue;}
		if(flag==false)
		x=x*10+a[i]-'0';
		else
		y=y*10+a[i]-'0';
	}
	return x*60+y;
}
bool myfunc(vector<int> x,vector<int> y)
{
if(x[0]<y[0])
return true;
if(x[0]==y[0])
{
	if(as[x[1]]<as[y[1]])
	return true;
}
return false;
}
main()
{
	//cout<<val("09:00");
	int t,cas=1;
	cin>>t;
	int aflag[201];
	vector<vector<int> > abe;
	vector<int> empty;
	while(t--)
	{
		int turn;
		abe.clear();
		//be.clear();
		cin>>turn;
		int na,nb;
		cin>>na>>nb;
		string x,y;
		int i;
		for(i=0;i<na;i++)
		{
			cin>>x>>y;
			as[i]=val(x);
			abe.push_back(empty);	
			abe[i].push_back(val(y));
			abe[i].push_back(i);
			abe[i].push_back(0);
		}
		for(i=na;i<na+nb;i++)
		{
			cin>>x>>y;
			as[i]=val(x);
			abe.push_back(empty);
			abe[i].push_back(val(y));
			abe[i].push_back(i);
			abe[i].push_back(1);
		}
		memset(&aflag,0,sizeof(aflag));
//		memset(&bflag,0,sizeof(bflag));
		int j;
		sort(abe.begin(),abe.end(),myfunc);
		//sort(be.begin(),be.end(),myfunc);
		//cout<<endl;
		//for(i=0;i<abe.size();i++)
		//cout<<as[abe[i][1]]<<" "<<abe[i][0]<<" "<<abe[i][2]<<endl;
		//cout<<endl;
		int mina,minb,aorb,start=0,end=0,k,acount=0,bcount=0;
      		for(i=0;i<na+nb;i++)
		{ 
		if(aflag[i]==1)
		 continue;	
                 aorb=abe[i][2];
		 start=as[abe[i][1]];
		 end=abe[i][0];
			end=end+turn;
		//cout<<aorb<<" "<<start<<" "<<end<<endl;
		if(abe[i][2]==0)
		acount++;	
		else
		bcount++;
		k=i;
		//cout<<endl<<abe[na+nb-1][0]<<endl;
		while(k<=na+nb-1)
		{
		  
		if(end>as[abe[k][1]] || (aorb)^(abe[k][2])==0 || aflag[k]==1)
                  {
		   k++;
		   continue;	
		  }
		 end=abe[k][0]+turn;
		 
   		 start=as[abe[k][1]];
		 aorb=abe[k][2];
		//cout<<aorb<<" "<<start<<" "<<end<<endl;
		 aflag[k]=1;
                 k++;
		}
		//cout<<"here"<<endl;

		
		} 
	cout<<"Case #"<<cas<<": "<<acount<<" "<<bcount<<endl;
    	cas++;
	}
}
