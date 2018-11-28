#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
int main()
{
     
    freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	vector<char> v;
	
	char a[500];
	int n,j,i;
	cin>>n;
	if(n<1 || n>30)
	cin>>n;
	j=0;
	while(gets(a))
	{             if(strlen(a)>100)
	              gets(a);
                  i=0;
                  j++;
                  while(a[i]!='\0')
                  {
                                   v.push_back(a[i]);
                                   i++;
                  }
                  v.push_back('$');
                  
                  if(j==n+1)
                  break;
    }
    
    int t=0;
	for(i=0;i<v.size()-1;i++)
	{
                            if(v[i]=='$')
                            {
                                         t++;
                                       if(i>0)
                                       cout<<endl; 
                                         cout<<"Case #"<<t<<": ";
                                         
                                         i++;
                            }
 
                               
                                  switch (v[i])
                                {
                                       case 'e':cout<<"o";
                                       break;
                                       case 'j':cout<<"u";
                                       break;           
                                                                    case 'p':cout<<"r";
                                break;
                                case 'm':cout<<"l";
                                break;
                                case 'y':cout<<"a";
                                break;
                                case 's':cout<<"n";
                                break;
                                case 'l':cout<<"g";
                                break;
                                
                                case 'c':cout<<"e";
                                break;
                                
                                case 'k':cout<<"i";
                                break;
                                case 'd':cout<<"s";
                                break;
                                case ' ':cout<<" " ;
                                break;
                                
                                case 'x':cout<<"m";
                                break;
                                case 'v':cout<<"p";
                                break;
                                case 'n':cout<<"b";
                                break;
                                case 'r':cout<<"t";
                                break;
                                case 'i':cout<<"d";
                                break;
                                
                                case 'b':cout<<"h";
                                break;
                                case 't':cout<<"w";
                                break;
                                case 'a':cout<<"y";
                                break;
                                case 'h':cout<<"x";
                                break;
                                case 'w':cout<<"f";
                                break;
                                case 'f':cout<<"c";
                                break;
                                
                                
                                case 'o':cout<<"k";
                                break;
                                
                                case 'u':cout<<"j";
                                break;
                                
                                case 'g':cout<<"v";
                                break;
                                case 'q':cout<<"z";
                                break;
                                case 'z':cout<<"q";
                                break;
                                
                                default:;cout<<a[i];
                                break;        }
}
        
	
 return 0;
                        
}                         
                           
                  
	
	
