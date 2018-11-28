#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    char orig[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
    char rep[27]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' '};
    int i,j,k,n;
    i=0;
    ifstream file1;
    string str;
    //char st[100];
    file1.open("a.in",ios::in);
    getline(file1,str);
    n=atoi(str.c_str());
    //cout<<n<<endl;
    while(file1.good())
    {
                       getline(file1,str);
                       //cout<<"!";
                       if(str=="")
                       continue;
                       for(j=0;(unsigned)j<str.length();j++)
                       {
                           //cout<<str[i];
                           //cout<<strlen(str[i]);
                           //cout<<str[j];
                           if(str[j]==' ')
                           continue;
                           k=strchr(rep,str[j])-rep;
                           str[j]=orig[k];
                           //cout<<"!";
                           }
                           cout<<"Case #"<<++i<<": "<<str<<endl;
                       }
    system("pause");
}
