#include<iostream>
using namespace std;

 
long check(string,string);
long l;
int main()
{
	long d,n,i,cnt,kase=0,j ;
	string *dic,test,str;
	cin>>l>>d>>n;	
	//while(cin>>l>>d>>n)
	//{
		dic = new string[d];
		for(i=0;i<d;i++) cin>>dic[i];
		for(i=0;i<n;i++) 
		{
			 cin>>test; 
			 cnt = 0;
			 for(j=0;j<d;j++) 
			 {str = dic[j]; cnt += check(str,test);}
			 cout<<"Case #"<<i+1<<": "<<cnt<<endl;
		}
	//}
	return 0;
}


long check(string dic,string word)
{  
   long    d =0, w =0,l = dic.size(), done = 0;
   string str;	
   while(d<=l)		
   {
       if(word[w]=='(')
       {  s1:
	  done = 0;
	  
          while(word[w]!=')')
	  {
		if(word[w]==dic[d]&&done == 0)
		{d++;str = str+word[w];done = 1;} 
		w++;
	  }
       }
       else
       {
	 
	 if(word[w]==')') w++; if(word[w]=='(') goto s1;  
	 if(word[w]==dic[d]) { str = str+word[w];}
	 w++;d++;
	}
   } 
	 if(str.size()-1==l)	return 1; else return 0;	
}
   	
