#include <iostream>
#include "math.h"
#include <fstream>


using namespace std;

int main()
{
    string st="";
   ifstream file( "input2.txt" );
   if(file==NULL)
   cout<<"ERROR"<<endl;
   ofstream myfile;
    myfile.open ("output2.txt");
    string fileString="";
    int nol=1;
//   flush(s);
   getline( file, st );
  // getline( file, s );
   //cout<<s<<endl;
   st.empty();
   while( getline( file, st ) )
   {
    char s1[100];
    const char *p1 = st.c_str();
    int i=0, noov=0, a, b;
    //cout<<st<<endl;
    while (*p1 != '\0')
    {
        //cout<<*p1<<"        "<<(int)*p1<<endl;
        if(*p1!=32)
        {
            s1[i]=*p1;
            *p1++;
            i++;
        }
        else
        {

            s1[i]='\0';
            if(noov==0)
            {*p1++; a = atoi(s1); noov++;}
            else
            break;
            i=0;

        }


    }
    s1[i]='\0';
    b=atoi(s1);
    //cout<<a<<endl<<b;
    //cin>>b;
    //int a=100;
    //int b=500;
    //int c=(a+b)/2;
    int no=0;
    for(int i=a; i<b; i++)
    {
        char buffer[33];
        itoa (i,buffer,10);
        string s="";
        s=s+(string)buffer;
        int siz = s.size();
        int e=ceil(pow(10,siz-1));
        int p=i;
        int q[siz];
        int lopco=0;
        for(int j=1; j<siz; j++)
        {
             //cout<<p<<endl;
             int d=(p%10);

             int f=p/10;
             //cout<<d<<" "<<e<<" "<<f<<endl;

            //p=((p%10)*pow(10,siz-1))+(p/10);
            p=d*e+f;
            //cout<<p<<endl;
            if(p>i && p<=b)
            {
                if(j==1)
                {//cout<<++no<<"       "<<i<<"      "<<p<<endl;
                 q[lopco]=p;
                 lopco++;
                 no++;
                }
                else
                {
                    int ch=0;
                    for(int var=0; var<lopco; var++)
                    {
                        if(q[var]==p)
                        {ch=1; break;}
                    }
                    if(ch==0)
                    {
                        q[lopco]=p;
                        lopco++;
                        no++;
                    }


                }

                //break;
            }
        }
        //int t;
        //cin>>t;
    }
    //cout<<endl<<no<<endl;
        fileString=fileString+"Case #";
        char buffer[33];
        itoa (nol,buffer,10);
        fileString=fileString+(string)buffer;
        fileString=fileString+": ";
        nol++;
        char buff[33];
        itoa (no,buff,10);
        fileString=fileString+(string)buff;
        myfile << fileString;
        st.empty();
        myfile<< "\n";
        fileString="";
   }//end of whileloop
   myfile.close();
    //cout<<sizeof(int);
    return 0;
}
