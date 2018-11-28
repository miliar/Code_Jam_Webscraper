# include<iostream>
# include<cstdio>
# include<cstring>
# include<fstream>
# include<sstream>
using namespace std;
int main()
{
    int t,i,j,k;
    char c[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
                   
    //             fflush(stdin);
    
    freopen("sub.in","r",stdin);
    cin>>t;
    
                 ofstream myfile;                 
                 myfile.open ("speaking.txt");
                 i=0;
                 cin.ignore();
                 //myfile<<t;
                 while(t--)
                 {
                           ++i;
                           string s;
                           getline(cin,s);    
                                        
                           myfile<<"Case #"<<i<<": ";
                           for(j=0;j<s.length();++j)
                           {
                                            if(s[j]!=' ')
                                            {
                                            k=int (s[j]-'a');
                                            myfile << c[k];
                                            }
                                            else
                                            myfile << s[j];
                           }
                 myfile << endl;
                 }
    myfile.close();
    
    return 0;
}
