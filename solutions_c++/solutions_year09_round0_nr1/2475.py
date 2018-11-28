#include<iostream>
#include<string>
#include<set>
using namespace std;
set<string> diction[15] ;
static int res=0;
int function(string str[],int size,int th);
static string nowget="";
int main()
{

    int L,D,N;
    string test_cha[16];
    char getcha;
    string singalstr;
    cin>>L>>D>>N;
    string::size_type p1=0,p2;
    for(int i = 0 ; i < D ; i++ )
    {
        for(int j = 0 ; j < L ; j++ )
        {
            cin>>getcha;
            singalstr+=getcha;
            diction[j].insert(singalstr);
        }
       // cin>>getcha;
        singalstr="";
    }
    int m=0;
    int result=0;
    int j;
    int len=0;
	char in=0;
    for( int i = 0 ; i < N ; i++ )
    {
            m=0;
            for(int l=0; l<16;l++)
            {
                test_cha[l]="";
            }

            cin >> singalstr ;

            len=singalstr.length();
            for(int k=0; k<len; k++)
            {
                getcha = singalstr.at(k);
                if(getcha=='(')
				{
					in=1;
					continue;
				}
                if(getcha == ')')
                {
                    m++;
					in=0;
                    continue;
                }
                test_cha[m]+=getcha;
				if(in==0)
					m++;
            }
            result=res=0;
            nowget="";
            function (test_cha,L,0);
			result=res;
        cout<<"Case #"<<i+1<<": "<<result<<endl;

    }


    return 0;
}

int function(string str[],int size,int th)
{


    if (size==th) return ++res;
   int len=str[th].length();
    for(int i=0;i<len;i++)
    {
        nowget+=str[th].at(i);
        int len2=nowget.length();
        if(diction[len2-1].find(nowget)!=diction[len2-1].end())
            function(str,size,th+1);
        nowget.erase(len2-1);
    }

}
