#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
//    freopen("C:\\Users\\pankaj\\Desktop\\codejam\\out.txt","w",stdout);
 //   freopen("C:\\Users\\pankaj\\Downloads\\A-small-attempt0.in","r",stdin);
    
    int t;
    string s,s3=" ";
    char s2[1000];
    char ch;
    scanf("%d",&t);
    getchar();
    int count=0;
    while(t--)
    {
        count++;
        getline(cin,s);
        //cout<<s;
        //getchar();
        s3="";
        for(int i=0;i<s.length();i++)
        {
            ch=s[i];
            if(ch!=' '&&ch!='\n')
            {
            switch(ch)
            {
            case 'a':
                s2[i]='y';
                break;
                case 'b':
                s2[i]='h';
                break;
                case 'c':
                s2[i]='e';
                break;
                case 'd':
                s2[i]='s';
                break;
                case 'e':
                s2[i]='o';
                break;
                case 'f':
                s2[i]='c';
                break;
                case 'g':
                s2[i]='v';
                break;
                case 'h':
                s2[i]='x';
                break;
                case 'i':
                s2[i]='d';
                break;
                case 'j':
                s2[i]='u';
                break;
                case 'k':
                s2[i]='i';
                break;
                case 'l':
                s2[i]='g';
                break;
                case 'm':
                s2[i]='l';
                break;
                case 'n':
                s2[i]='b';
                break;
                case 'o':
                s2[i]='k';
                break;
                case 'p':
                s2[i]='r';
                break;
                case 'q':
                s2[i]='z';
                break;
                case 'r':
                s2[i]='t';
                break;
                case 's':
                s2[i]='n';
                break;
                case 't':
                s2[i]='w';
                break;
                case 'u':
                s2[i]='j';
                break;
                case 'v':
                s2[i]='p';
                break;
                case 'w':
                s2[i]='f';
                break;
                case 'x':
                s2[i]='m';
                break;
                case 'y':
                s2[i]='a';
                break;
                case 'z':
                s2[i]='q';
                break;
                
            }   
        }
        else if(ch==' ')
        {
        s2[i]=ch;  
        } 
        if(ch!='\n') 
        s3=s3+s2[i];   
        //cout<<s3<<endl;   
        }
        cout<<"Case #"<<count<<": "<<s3<<endl;
        ///getchar();
    }
    //system("pause");
    return 0;
}
