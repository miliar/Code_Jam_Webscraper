
// Headers {{{
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define CLR(A,v) memset((A),v,sizeof((A)))
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(x) (int)(x.size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD; 
typedef vector<string> VS;
// }}}

const int buf_size = 10000000; 
char buf[buf_size]; 

VS split(string x) { 
    x += " "; 
    string tmp = ""; 
    VS ret; 
    FORE(e,x) if (*e != ' ') tmp += *e; 
    else if (SIZE(tmp)) { 
        ret.PB(tmp); 
        tmp = "";
    } 
    return ret; 
} 

string all; 

void skip(int &pos) { 
     while (pos < SIZE(all) && (all[pos] == '(' || all[pos] == ')' || all[pos] == ' ')) ++pos; 
} 

LD get_dub(int &pos) { 
    LD ret = all[pos] - '0', pw = 1.0; 
    ++pos; 
    if (all[pos] == '.') { 
        ++pos; 
        while (isdigit(all[pos])) {         
            pw /= 10; 
            ret += pw * (all[pos] - '0'); 
            ++pos; 
        } 
    } 
    return ret; 
} 

class tree { 
    public : 
        string feature; 
        LD pr; 
        tree *lf, *rg; 

        void read(int &pos) { 
            skip(pos); 
            feature = ""; 
            pr = get_dub(pos); 
            skip(pos);        

            if (isalpha(all[pos])) { 
                while (isalpha(all[pos])) { feature += all[pos]; ++pos; }              
                lf = new tree(); 
                lf->read(pos); 
                rg = new tree(); 
                rg->read(pos); 
            }            
            else {               
                lf = NULL; 
                rg = NULL; 
            }   
        } 
        
        void write() { 
            printf("%s %Lf{\n",feature.c_str(),pr); 
            if (lf != NULL) { 
                lf->write(); 
                rg->write(); 
            } 
            puts("}"); 
        }  

        LD get_prob(const set<string> &ss) {
            if (!SIZE(feature)) return pr; 
            if (ss.count(feature)) return pr * lf->get_prob(ss); 
            else return pr * rg->get_prob(ss); 
        } 

        void del() { 
            if (lf != NULL) delete lf; 
            if (rg != NULL) delete rg; 
        } 

        ~tree() { 
            if (lf != NULL) delete lf; 
            if (rg != NULL) delete rg; 
        } 
} W; 
int T, L; 

int main()
{
  scanf("%d", &T); 
  
    FOR(tc, 1, T) { 
        all = ""; 
        scanf("%d",&L); 
        fgets(buf, buf_size - 1, stdin);  
        REP(i,L) { 
            fgets(buf, buf_size - 1, stdin); 
            REP(j,buf_size) if (buf[j] == 10 || buf[j] == 13) break; 
                else  all += buf[j];            
        } 
        //puts(all.c_str());  
         
        int pos = 0, cnt, ff; 
        W.read(pos);  
        //W.write(); 
        printf("Case #%d:\n",tc); 
        scanf("%d",&cnt); 
        set<string> ss; 

        while (cnt--) { 
            ss.clear(); 
            scanf("%s%d",buf,&ff); 
            while (ff--) { 
                scanf("%s",buf); 
                ss.insert(buf);                 
            } 
            printf("%.10Lf\n",W.get_prob(ss)); 
        } 
         

    } 



	return 0;
}

