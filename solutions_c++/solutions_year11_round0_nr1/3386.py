#include "template"

int o[100][2],b[100][2];
int ora,blu;

int find()
{
	int curb,curo,i,j,tmp,m,n,no,t;
	curb=curo=1;
	i=0;j=0;
	no=1;
	int time=0;
	while(i<ora && j<blu)
	{
		//cout<<curo<<" "<<curb<<endl;
		t=1;
		if(o[i][1]==no)
		{
			m=abs(o[i][0]-curo);
			m++;
			n=abs(b[j][0]-curb);
			tmp=min2(m,n);
			if(b[j][0]<curb)
				t=-1;
			curb+=(t*tmp);
			curo=o[i][0];
			time+=m;
			i++;
		}
		else
		{
			m=abs(b[j][0]-curb);
			m++;
			n=abs(o[i][0]-curo);
			tmp=min2(m,n);
			if(o[i][0]<curo)
				t=-1;
			curo+=(t*tmp);
			curb=b[j][0];
			time+=m;
			j++;
		}
		no++;
	}
	if(j==blu)
	{
		
		while(i<ora)
		{
		//cout<<curo<<" "<<curb<<endl;
			time+=abs(curo-o[i][0]);
			time++;
			curo=o[i][0];
			i++;
		}
	}
	else if(i==ora)
	{
		while(j<blu)
		{
		//cout<<curo<<" "<<curb<<endl;
			time+=abs(curb-b[j][0]);
			time++;
			curb=b[j][0];
			j++;
		}
	}
	return time;
}

int main()
{
	int t,i,j,k,n;
	
	cin>>t;
	char x;
	REP(i,t)
	{
		ora=0;
		blu=0;
		cin>>n;
		REP(j,n)
		{
			cin>>x;
			if(x=='O')
			{
				cin>>k;
				o[ora][0]=k;
				o[ora][1]=(j+1);
				ora++;
			}
			else if(x=='B')
			{
				cin>>k;
				b[blu][0]=k;
				b[blu][1]=(j+1);
				blu++;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<find()<<endl;
	}
	return 0;
}
