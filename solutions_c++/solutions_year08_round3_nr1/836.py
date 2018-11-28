#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 1100
#define maxp 1100000

string toUpperString(string text)
{
string toReturn(text); // duplicate input for manipulation

for(int i=0;i<text.length();++i) // for each character in string
{
toReturn[i]=toupper(text[i]); // convert char to uppercase
}

return toReturn; // return in upper case
}

void splitstring(string str, string seperater, string &first, string &second) //will split a string into 2
{
     int i = (int)str.find(seperater); //find seperator
     if(i != -1)
     {
          int y = 0;
          if(!str.empty())
          {
               while(y != i)
               {
                    first += str[y++]; //creating first string
               }
               y = y+(int)seperater.length(); //jumping forward seperater length
               while(y != str.length())
               {
                    second += str[y++]; //creating second string
               }
               
          }
     }
     else
     {
          first = str;
          second = "NULL"; //if seperator is not there then second string == null 
     }
}

int PrimeFactors (LL n,LL p,LL *temp2,LL& length)
{
	
	LL count = 0, kp=0;
//	LL temp = 0;
	
	
	for ( LL i = 1 ; i <= n ; i++ )
	{
		
		LL j = i - 1;
		
		while ( j > 1 )
		{
			if ( i % j == 0 )      //Is PRIME
				break;
			else
				j--;
		}
		
		if ( j == 1 )
		{
		//  if(n >= i) {
            if ( n % i == 0 )
			{
			 cout<<"\n"<<i<<" n "<<n<<" ";    //PRIME factor 
		//	 	if (i>=n) return 0;
				if ( i >= p ) {
                     cout<<i<<endl;
            //         system("PAUSE");
                     temp2[kp] = i;
                     kp++;
                     length = kp;
                     }
               }             
			}
	//	}

	}
  return 0;  
}

string tr[500000],a22[500000];

int main() {
    string line;
        int w=0,acc=0;
  ifstream jam;
  jam.open("C:/round1/A-small-attempt1.in", ios::in);
  if (jam.is_open()) {
    while (! jam.eof() ) {
      getline (jam,line);
      tr[w] = line;
      a22[w] = line;
      w++;
    }
    jam.close();
  }

//  
  ofstream jam_o;
  jam_o.open("C:/round1/a.out.txt", ios::out);

  
  int T;
  T = atoi(tr[acc].c_str());
  cout<<endl<<T<<endl;
//  system("PAUSE");
//  acc++; //=1
  REP(C,T) {

         int res = 0,l,length,wq=0,sig=0,j=0,pa,ka; 
         int temp1[10],temp2[1100];
//         LL a,b,p,temp1[4],temp4[50000],len1,len2,sets,temp2[50000],temp3[50000];
         string a1[50000],a2[50000],a11;
//         cout<<acc<<endl;
//         system("PAUSE");
         for(int i=0;i<10;i++) {
                     temp1[i] = 0;
//                     temp2[i] = 0;
//                     temp3[i] = 0;
//                     temp4[i] = 0;
//                     a1[i] = ""; //init others to if reqd
//                    
                   }
                   REP(i,1100) {
                       temp2[i] = 0; }
                   REP(i,50000) {
                                a1[i] = "";
                                a2[i] = ""; }
      
         acc++; //=1
        // cout<<acc<<endl;
        // system("PAUSE");
         for(int e = 0;e<3;e++) { //cout<<endl<<a22[acc];   //split ips in a line and convert to int
                    splitstring(a22[acc], " ",a1[e],a11); 
                    temp1[e] = atoi(a1[e].c_str());
                    cout<<endl<<a1[e];
                    a22[acc] = a11;
                    a11 = "";
                    }
                    //system("PAUSE");
          
          pa = temp1[0];          
          ka = temp1[1];
          l = temp1[2];
          
          acc++;//2
           for(int e = 0;e<l;e++) { //cout<<endl<<a22[acc];   //split ips in a line and convert to int
                    
                    splitstring(a22[acc], " ",a2[e],a11); 
                    temp2[e] = atoi(a2[e].c_str());
                    cout<<endl<<temp2[e];
                    a22[acc] = a11;
                    a11 = "";
                    }
//                    system("PAUSE");
          
         int tmp;

for (int i=0; i<l-1; i++) {
  for (int j=0; j<l-1-i; j++)
    if (temp2[j+1] > temp2[j]) {  /* compare the two neighbors */
      tmp = temp2[j];         /* swap a[j] and a[j+1]      */
      temp2[j] = temp2[j+1];
      temp2[j+1] = tmp;
  }
}

REP(i,l) { cout<<endl<<"t2 "<<temp2[i];}
//system("PAUSE");

  for(int i=0;i<pa;i++) {
           for(int j=0;j<ka;j++) {
                  
                    if (sig == l)
                    {   cout<<"gone";
                        goto l1;}
                    cout<< temp2[sig]<<"i+j "<<i<<" "<<sig<<endl;
                    res += (i+1)*temp2[sig];
                    cout<<" res "<<res;
                      sig++;
//                    system("PAUSE");
                    }
           }

    l1:   ;//  cout<<" C "<<C;
//         system("PAUSE");
                 
  jam_o << "Case #"<<C+1<< ": "<< res<<endl;  


}
  jam_o.close();           
}



