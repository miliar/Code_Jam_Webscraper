#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <fstream>
#include <numeric>
#include <math.h>

using namespace std;

typedef long long  ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<string,string> ss;

typedef vector<char> vc;
typedef vector<vc> vvc;
typedef pair<char,char> cc;

typedef vector<bool> vb;
typedef vector<ll> vll;
#define sz(v) int((v).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define ALL(C) (C).begin(), (C).end()
#define INF numeric_limits<int>::max()
#define MINF numeric_limits<int>::min()
#define PRTV(c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++){ cout<<*i<<" "; } cout<<endl;
#define DB(C) if(0){std::cout<<#C <<" = "<< (C)<<std::endl;}

int casenum;


ll doitsmall ( ll R, ll K,ll N, vll & me)
{
    ll sum = 0 ;
    ll iter  =0;
    int pos  = 0;
    ll pp;
    for ( iter =0; iter <  R ; ++iter )
    {
        pp = 0;
            int added = 0;
        while ( pp + me[pos] <= K && added < N)
        {


            pp += me[pos];
            sum +=me[pos];
     //cout<<R<<K<<N<<" " <<iter<<" " <<"adding " <<pos <<" " << me[pos]<<" " << sum <<endl;
            ++pos ;
                pos = pos % N;
            added++;

        //
            }

    }
    return sum;

    }

ll doit ( ll R, ll K,ll N, vll & me)
{
    ll sum = 0 ;
    ll iter  =0;
    int pos  = 0;
    ll pp;
    int lastpos;
    //map < ll , pair<ll , ll > > his;
    vll hissum;
    vll hispos;

    // loop o , sum 0, ptr to pos0
    hissum.push_back(0);
    hispos.push_back(-1);

    bool loop = false;
    for ( iter =1; iter <=  R ; ++iter )
    {
     //   cout<< iter << " for  " << sum << endl;
        pp = 0;
        int added = 0;


        while ( pp + me[pos] <= K && added < N)
        {


            pp += me[pos];
            sum +=me[pos];
            added++;
             ++pos ;
                pos = pos % N;
            }


        lastpos = pos > 0 ? pos-1: N-1;

        if ( find(ALL (hispos), lastpos) == hispos.end())
        {
            hispos.push_back(lastpos);
            hissum.push_back(sum);
          // cout<< "add : iter " << sz(hispos) -1 << " " << lastpos << " " << sum<< endl;
            continue;
            }
        else {
            loop = true;

           // cout<<"loop " << iter << " " << lastpos << " " << his[lastpos].first<<" " << his[lastpos].second<<endl;
            break;
            }

    }



    if ( !loop)
        {
         //  cout<<"nolop used : " <<sum<<endl;
            return sum;}



    ll lt = find(ALL (hispos), lastpos) - hispos.begin ();
        DB(lt);
    ll dt = iter - lt;
      DB(dt);
    ll ds = sum - hissum[lt];
     DB(ds);
  //  cout<< hissum[lt]<<endl;
  //  cout<<  ds * (int) ((R - lt) / ( dt )) <<endl;
    ll tt = ds * (int) ((R - lt) / ( dt )) + hissum[lt];
     DB(tt);


    cout<< " lop met" << endl;




   // ll st = ( (R-  his[lastpos].first)/ ( iter - his[lastpos].first))  * (sum - his[lastpos].second);
    //cout<< " loop caught : " << ( (R-  his[lastpos].first)/ ( iter - his[lastpos].first)) << " " << (sum - his[lastpos].second) << "  "<<st << endl;

    //st+=  his[lastpos].second;

    //pos = (lastpos +1) % N;
    for ( iter  = (R-  lt) %(dt) ; iter >0; --iter )
    {
        cout<< "residual " <<endl;
        DB(iter);
        DB(pos);

        pp = 0;
        int added = 0;
        while ( pp + me[pos] <= K && added < N)
        {
          //  cout<< "add residual  = " << pos << " " << me[pos] <<endl;

            pp += me[pos];
            tt +=me[pos];
            ++pos ;
                pos = pos % N;
            added++;


            }

        };

   return tt;

    };


int main()
{
ifstream infile ("A-large-practice.in");
ofstream outfile ("output.txt");

string line;
int linecnt =0 ;
if (infile.is_open())
	{
	    do{
			getline (infile,line);
			++linecnt;
			if (!(line.size () > 0))
				break;
				istringstream r(line);


                // from here process the input content
                if(1==linecnt){
                    r>> casenum;
                    }


                else{

                        ll R,K,N;

                        r>>R >> K >> N;

                        getline (infile,line);
                        istringstream p(line);
                        ll s;
                        vll me;
                        while ( p >> s)
                        {
                            me.push_back(s);
                            }

                       // outfile<<"Case #"<<(linecnt -1  )<<": "<<doit(R, K, N, me)<<" "<< doitsmall(R, K, N, me) <<" "<<  R <<" "<< N << " " << K <<endl;
                        outfile<<"Case #"<<(linecnt -1  )<<": "<<doit(R, K, N, me)<<endl;
                    }


            }while (! infile.eof() );


	infile.close();
	};

	    outfile.close();


    return 0;
}
