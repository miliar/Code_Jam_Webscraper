#include<cstring>
#include<iostream>

using namespace std;

class node
{
	public:
		char code;
		int value;
};

int main(void)
{
	
	int t;
	cin>>t;
	int test[t];
	memset(test,0,sizeof(test));
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		node arr[n];
		for(int l=0;l<n;l++)
		{
			cin>>arr[l].code;
			cin>>arr[l].value;
		//	printf("(%d,%c,%d\n)",l,(arr[l].code),(arr[l].value));
			
		}
		//for(int l=0;l<n;l++)
	//		printf("(%d,%c,%d)",l,(arr[l].code),(arr[l].value));
		int pos_b=1,pos_o=1,o=0,b=0,ans=0;
	//	printf("%d%d%d%d%d\n",pos_o,pos_b,o,b,ans);
		for(int h=0;h<n;h++)
		{
			int temp =0;
			while(true)//dhyAN RAKHNA
			{
				if(o>n)
					break;
				if(arr[o].code=='O')
					break;
				o++;
			}
			while(true)
			{
				if(b>n)
					break;
				if(arr[b].code=='B')
					break;
				b++;
			}
	//		cout<<"ob pair"<<o<<b<<endl;
			if(arr[h].code=='O')
			{
		//		cout<<"in o\n";
				if(arr[h].value>=pos_o)
				{
					temp=arr[h].value-pos_o+1;
					ans+=temp;
				}	
				else 
				{
					temp=pos_o-arr[h].value+1;
					ans+=temp;
				}
				if(arr[b].value<pos_b)
				{
					if(pos_b-temp<=arr[b].value)
						pos_b=arr[b].value;
					
					else
						pos_b-=temp;
				}
				else
				{
					if(pos_b+temp>=arr[b].value)
						pos_b=arr[b].value;
				
					else
						pos_b+=temp;
				}
				pos_o=arr[h].value;
				o++;
			}
			else if(arr[h].code=='B')
			{
	//			cout<<"in b\n";
				if(arr[h].value>=pos_b)
				{
					temp=arr[h].value-pos_b+1;
					ans+=temp;
				}
				else 
				{
					temp=pos_b-arr[h].value+1;
					ans+=temp;
				}
				if(arr[o].value<pos_o)
				{
					if(pos_o-temp<=arr[o].value)
						pos_o=arr[o].value;
					
					else
						pos_o-=temp;
				}
				else
				{
					if(pos_o+temp>=arr[o].value)
						pos_o=arr[o].value;
				
					else
						pos_o+=temp;
				}
				b++;
				pos_b=arr[h].value;
			}	
			//cout<<pos_o<<pos_b<<o<<b<<ans<<endl;
		}
		test[i]=ans;
		
		
	}
	for(int i=0;i<t;i++)
	{
	//	printf("Case #%d:%d\n",i+1,test[i]);
		cout<<"Case #"<<i+1<<": "<<test[i]<<"\n";
	}
	return 0;
}