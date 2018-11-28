#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<iterator>
#include<functional>
#include<time.h>
#include<iomanip>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll diff(ll a,ll b)
{
    return a>b ? a-b : b-a;
}

/*#define COMB_NUM 10001L
ll comb[COMB_NUM][COMB_NUM];
//need init_comb();
void init_comb()
{
    comb[0][0]=1;
    ll i,j;
    for(i=1;i<COMB_NUM;i++)
    {
        comb[i][0]=comb[i][i]=1;
        for(j=1;j<i;j++)
            comb[i][j]=comb[i-1][j]+comb[i-1][j-1];
    }
}
*/

#define print(a)      for(int i=0;i<a.size();i++) cout<<a[i]<<" "; cout<<endl;
#define print2n(a,n)      for(int i=0;i<=n;i++) cout<<a[i]<<" "; cout<<endl;

void llFromString(const string &s,ll &a,ll &b)
{
    string replacedString = s;
    replace_if(replacedString.begin(),
               replacedString.end(),
               bind2nd(equal_to<char>(),'.'),
               ' ');
               
    istringstream buffer(replacedString);
    buffer>>a;
    if(buffer.good())
    {
        buffer>>b;
    }
    else
    {
        b=0;
    }
}


template<class T>
vector<T> split(const std::string &s) {
    
    string replacedString = s;
    replace_if(replacedString.begin(),
               replacedString.end(),
               bind2nd(equal_to<char>(),'.'),
               ' ');
    
    vector<T> ret;
    istringstream buffer(replacedString);
    copy(istream_iterator<T>(buffer),
         istream_iterator<T>(), back_inserter(ret));
    return ret;    
}// vector<ll> k = split<ll>(s);

int main()
{
	fstream in,out;
	//in.open("test.in.txt",ios::in); out.open("test.out.txt",ios::out);
	//in.open("A-small-attempt0.in",ios::in); out.open("A-small-0.out",ios::out);
	  in.open("A-large.in",ios::in); out.open("A-large-0.out",ios::out);

	istream& input = in;
	ostream& output = out;

	ll case_id,total_case,temp,ans;

	input>>total_case; 
	int I,H,K,L,N,k;     
	ll state;
	bool u[100];
	char token[5][5];
	for(case_id=1;case_id<=total_case;case_id++)
	{
        k = 0;
        for(I=0;I<4;I++)
        {
            input>>token[I];
            for(H=0;H<4;H++)
                if(token[I][H]!='.') k++;
        }
        
        state = 0;
        if(k==16) state = 3;
        
        int o,x,t;
        
        for(I=0;I<4;I++)
        {
            o=x=t=0;
            for(H=0;H<4;H++)
            {
                if(token[I][H]=='O') o++;
                if(token[I][H]=='X') x++;
                if(token[I][H]=='T') t++;
                
            }
            if(o+t==4) state = 2;
            if(x+t==4) state = 1;
        }
        
        for(H=0;H<4;H++)
        {
            o=x=t=0;
            for(I=0;I<4;I++)
            {
                if(token[I][H]=='O') o++;
                if(token[I][H]=='X') x++;
                if(token[I][H]=='T') t++;
                
            }
            if(o+t==4) state = 2;
            if(x+t==4) state = 1;
        }
        
        o=x=t=0;
        for(I=0;I<4;I++)
        {
            if(token[I][I]=='O') o++;
            if(token[I][I]=='X') x++;
            if(token[I][I]=='T') t++;
  
            if(o+t==4) state = 2;
            if(x+t==4) state = 1;
        }
        
        o=x=t=0;
        for(I=0;I<4;I++)
        {
            if(token[I][3-I]=='O') o++;
            if(token[I][3-I]=='X') x++;
            if(token[I][3-I]=='T') t++;
  
            if(o+t==4) state = 2;
            if(x+t==4) state = 1;
        }
        
		output<<"Case #"<<case_id<<": ";
		//output<<ans;
		switch(state)
		{
            case 0:
                output<<"Game has not completed";
                break;
            case 1:
                output<<"X won";
                break;
            case 2:
                output<<"O won";
                break;
            case 3:
                output<<"Draw";
                break;
            default:
                output<<"!!!";
        }
		output<<endl;
	}
    //system("PAUSE");
    return EXIT_SUCCESS;
}
