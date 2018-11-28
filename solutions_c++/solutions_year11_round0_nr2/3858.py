#include<iostream>
#include<map>
using namespace std;

int main()
{
	int t;
	cin>>t;
   int count=0;
	while(t--)
	{
		int c,d;
		map<string,char> comp;
		map<char,char> oppose;
		cin>>c;
		char temp[10];
		string temp1="";
		int length=0;
		for(int i=0;i<c;i++)
		{
			cin>>temp;
			temp1="";
			temp1+=temp[0];
			temp1+=temp[1];
			comp[temp1]=temp[2];
       //     cout<<"\nadded**comp["<<temp1<<"]="<<comp[temp1];
			//swapped combinition
			temp1="";
			temp1+=temp[1];
			temp1+=temp[0];
			comp[temp1]=temp[2];
		//	cout<<"\nadded**comp["<<temp1<<"]="<<comp[temp1];
		}
		cin>>d;
		for(int i=0;i<d;i++)
		{
			cin>>temp;
			oppose[temp[0]]=temp[1];
			oppose[temp[1]]=temp[0];//reverse
		}
		cin>>length;
		char master[101];				
		cin>>master;
		string answer="";
		for(int i=0;i<length;i++)
		{
			if(answer.size()<1)
            {
				answer+=master[i];
                continue;
             }
                
			string str1="";
			str1+=master[i];
			str1+=answer[(int)answer.size()-1];
			//cout<<"\n**comp["<<str1<<"]="<<comp[str1];
            if(comp[str1]!=0)
			{	
				answer.erase(answer.end()-1,answer.end());
				answer+=comp[str1];
				continue;
			}
			int flag=0;
			for(int j=0;j<answer.size();j++)
			{
				if( oppose[master[i]]== answer[j])
				{
					flag=1;
					answer="";
					break;
				}
			}
			if(flag==0)
				answer+=master[i];
		}
	   if(answer!="")
	   {
            if(answer.size()== 1)
                {
                    cout<<"Case #"<<++count<<": ["<<answer[0]<<"]"<<endl;
                    }
                    else
                    {
                    		 cout<<"Case #"<<++count<<": ["<<answer[0]<<",";
                                for(int i=1;i<answer.size()-1;i++)
                                     cout<<" "<<answer[i]<<",";
                                     cout<<" "<<answer[answer.size()-1]<<"]"<<endl;
                    }
        }
        else
            cout<<"Case #"<<++count<<": []"<<endl;
  }
	return 0;
}
									
			


				
			
			
