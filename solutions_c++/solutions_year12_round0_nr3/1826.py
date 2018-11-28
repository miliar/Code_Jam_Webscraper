#include<iostream>
#include<vector>
#include<string>

using namespace std;
int recycled(const int a,const int b)
{
 	int num=a;
 	int n,m,i,count=0;
 	string s,s1;
 	vector<string> list;
 	
 	
 	while(num<b){
	  n=num;
	  while(n>0){
	    m=n%10;
        n/=10;
        s.insert(s.begin(),m+'0');
		}
      for(i=0,s1=s;i<s.size()-1;i++){
         s1.insert(s1.end(),s1[0]);
         s1.erase(s1.begin());
         list.push_back(s1);
         for(m=0;m<list.size()-1;m++)
           if(s1==list[m])  break;
           if(m!=list.size()-1) continue;
           
         
         for(m=n=0;m<s1.size();m++)
           n=10*n+s1[m]-'0';
         if(n>num && n<b){
           count++;
       cout<<num<<' '<<n<<endl;
		       }
		   }
		   num++;
		   list.clear();
		   s.clear();
		   s1.clear();
		}
		return count;
   // cout<<s;
}
        

   
int main()
{
 	  freopen("i.in","r",stdin);
 	  freopen("o.out","w",stdout);
     int n,i;
     cin>>n;
 	 int s[n][2];
 	 for(i=0;i<n;i++)
 	   cin>>s[i][0]>>s[i][1];
     for(i=0;i<n;i++)
       cout<<"Case #"<<i+1<<": "<<recycled(s[i][0],s[i][1])<<endl;
     
 	
 	
 	
 	
  //  system("pause");
 	return 0;
}
