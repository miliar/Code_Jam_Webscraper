        #include<iostream>
        using namespace std;
        
        bool function(string,string);
        int l;
        int main()
        {
        	int d,n,i,j,kount;
        	string *dictionary,t,str;
        	cin>>l>>d>>n;	
        	 dictionary = new string[d];
        		for(i=0;i<d;i++) cin>>dictionary[i];
        		for(i=0;i<n;i++) 
        		{
        			 kount = 0;
        			 cin>>t; 
        			 for(j=0;j<d;j++) 
        			 {str = dictionary[j]; kount += function(str,t);}
        			 cout<<"Case #"<<i+1<<": "<<kount<<endl;
        		 }
        	return 0;
        }
        
        
bool function(string dictionary,string kase)
{  
           int    d =0, w =0,finished = 0;
           string str;	
           while(d<=l)		
           {
               if(kase[w]=='(')
               {  s1:
        	  finished = 0;
        	  
             while(kase[w]!=')')
        	  {
        		if(kase[w]==dictionary[d]&&finished == 0)
        		{d++;str = str+kase[w];finished = 1;} 
        		w++;
        	  }
               }
               else
               {
        	 
        	 if(kase[w]==')') w++; if(kase[w]=='(') goto s1;  
        	 if(kase[w]==dictionary[d]) { str = str+kase[w];}
        	 w++;d++;
        	}
           } 
           if(str.size() == l+1)	return 1;  else return 0;	
        }
           	
