//#include<iostream>
//#include<queue>
//#include<time.h>
//#include<cmath>
//#include<math.h>
//using namespace std;
//const int N = 1008;
//const int INF = 1<<28;
//const int MaxSon = 4;
//
//struct Node{ int son[MaxSon], father, suffix; char ch; bool mark; }p[N];
//struct Point{
//	int ps, lv;
//	Point( int x, int y ){ ps = x; lv = y; }
//};
//int dp[N][N];
//int mat[101][101], t[101][101], tp[101][101];
//
//class Trie{
//public:
//	static void Init( char *cs, int *sign, int &pend, Node *p ){
//		for(int i=0; i<MaxSon; i++) sign[cs[i]] = i;
//		Init( pend, p, 0, '$' );
//	}
//	static void Init( int &pend, Node *p, int father, char ch ){
//		p[pend].father = father;
//		p[pend].ch = ch;
//		p[pend].mark = false;
//		for(int i=0; i<MaxSon; i++) p[pend].son[i] = -1;
//		pend++;
//	}
//	static void Insert( int *sign, int &pend, Node *p, char *s ){
//		int ps = 0, k = strlen( s );
//		for(int i=0; i<k; i++){
//			int u = sign[s[i]];
//			if( p[ps].son[u] == -1 ){
//				p[ps].son[u] = pend;
//				Init( pend, p, ps, s[i] );
//			}
//			ps = p[ps].son[u];
//		}
//		p[ps].mark = true;
//	}
//	static int Suffix( int *sign, int ps, Node *p ){
//		int t = p[ps].father;
//		if( t == 0 ) return 0;
//		int u = sign[p[ps].ch];
//		for(t=p[t].suffix; t!=0 && p[t].son[u]==-1; t=p[t].suffix);
//		if( p[t].son[u] == -1 ) return 0;
//		return p[t].son[u];
//	}
//	static void TrieGraph( int *sign, Node *p ){
//		queue<int> q; q.push( 0 );
//		p[0].suffix = 0;
//		while( !q.empty() ){
//			int u = q.front(); q.pop();
//			for(int i=0; i<MaxSon; i++){
//				int v = p[u].son[i];
//				if( v == -1 ) continue;
//				p[v].suffix = Suffix( sign, v, p );
//				p[v].mark = (p[v].mark||p[p[v].suffix].mark);
//				if( !p[v].mark ) q.push( v );
//			}
//			for(int i=0; i<MaxSon; i++){
//				if( p[u].son[i] != -1 ) continue;
//				p[u].son[i] = p[p[u].suffix].son[i];
//			}
//		}
//	}
//	/*static void Get_Matrix( int &pend, Node *p ){
//		memset( mat, 0, sizeof(mat) );
//		queue<int> q;
//		int *id = new int[pend], k = 0;
//		for(int i=0; i<pend; i++) id[i] = -1;
//		bool *vis = new bool[pend];
//		memset( vis, 0, sizeof(bool)*pend );
//		id[0] = k++; vis[0] = 1;
//		for( q.push(0); !q.empty(); ){
//			int u = q.front(); q.pop();
//			for(int i=0; i<MaxSon; i++){
//				int v = p[u].son[i];
//				if( v == -1 ){ mat[id[u]][0]++; continue; }
//				if( p[v].mark ) continue;
//				if( id[v] == -1 ) id[v] = k++;
//				mat[id[u]][id[v]]++;
//				if( !vis[v] ){ q.push( v ); vis[v] = 1; }
//			}
//		}
//		delete []vis;
//		delete []id;
//		pend = k;
//	}
//	static void Mul( int a[101][101], int b[101][101], int n ){
//		for(int i=0; i<n; i++){
//			for(int j=0; j<n; j++){
//				tp[i][j] = 0;
//				for(int k=0; k<n; k++){
//					tp[i][j] = (tp[i][j]+(__int64)a[i][k]*b[k][j])%100000;
//				}
//			}
//		}
//		memcpy( t, tp, sizeof(tp) );
//	}
//	static void Power( int n, int pend ){
//		if( n == 1 ) memcpy( t, mat, sizeof(mat) );
//		else{
//			Power( n>>1, pend );
//			Mul( t, t, pend );
//			if( n&1 ) Mul( t, mat, pend );
//		}
//	}
//	static void ans(){ // poj 2778 DNA Sequence
//		int n, m, sign[300];
//		char cs[5] = {"AGCT"}, s[12];
//		while( 2==scanf("%d%d",&n,&m) ){
//			int pend = 0;
//			Init( cs, sign, pend, p );
//			for(int i=0; i<n; i++){
//				scanf("%s",&s);
//				Insert( sign, pend, p, s );
//			}
//			TrieGraph( sign, p );
//			Get_Matrix( pend, p );
//			Power( m, pend );
//
//			int res = 0;
//			for(int i=0; i<pend; i++) res = (res+t[0][i])%100000;
//			printf("%d\n",res);
//		}
//	}*/
//	/*static void Solve( char *cs, int len, char *s, int pend, Node *p ){
//		queue<Point> q;
//		q.push( Point( 0, 0 ) );
//		for(int i=0; i<pend; i++) for(int j=0; j<N; j++) dp[i][j] = INF;
//		dp[0][0] = 0;
//		while( !q.empty() ){
//			Point t = q.front(); q.pop();
//			if( t.lv == len ) break;
//			for(int i=0; i<MaxSon; i++){
//				int u = p[t.ps].son[i];
//				if( u == -1 ) u = 0;
//				if( p[u].mark ) continue;
//				bool flag = (dp[u][t.lv+1]==INF);
//				dp[u][t.lv+1] = min( dp[u][t.lv+1], dp[t.ps][t.lv]+(s[t.lv]!=cs[i]) );
//				if( flag ) q.push( Point( u, t.lv+1 ) );
//			}
//		}
//		int md = INF;
//		for(int i=0; i<pend; i++) md = min( md, dp[i][len] );
//		if( md == INF ) printf("-1\n");
//		else printf("%d\n", md );
//	}
//	static void ans(){ // poj 3691 DNA repair
//		int n, t = 0, sign[300];
//		char cs[5] = {"AGCT"}, s[1008];
//		while( scanf("%d",&n)!=EOF && n!=0 ){
//			int pend = 0;
//			Init( cs, sign, pend, p );
//			for(int i=0; i<n; i++){
//				scanf("%s",s );
//				Insert( sign, pend, p, s );
//			}
//			TrieGraph( sign, p );
//
//			scanf("%s",s);
//			printf("Case %d: ",++t);
//			Solve( cs, strlen(s), s, pend, p );
//		}
//	}*/
//};
//
//class Palindromes{
//	struct Node{
//		int ch[26], t, s; char c;
//		void set( char C ){ memset( ch, -1, sizeof(int)*26 ); t = s = 0; c = C; }
//	};
//public:
//	static void Insert( int ps, int &pn, Node *p, int n, char *s, bool *ok ){
//		for(int i=0; i<n; i++){
//			int v = s[i]-'a';
//			if( p[ps].ch[v]==-1 ){ p[++pn].set( s[i] ); p[ps].ch[v] = pn; }
//			ps = p[ps].ch[v];
//			if( i<n-1 && ok[i+1] ) p[ps].s++;
//		}
//		p[ps].t++;
//	}
//	static void Show( int ps, Node *p, int deep ){
//		for(int i=0; i<26; i++){
//			if( p[ps].ch[i] != -1 ) Show( p[ps].ch[i], p, deep+1 );
//		}
//		for(int i=0; i<deep; i++) printf(" "); printf("%c %d %d\n",p[ps].c,p[ps].t,p[ps].s);
//	}
//	// a[i] = { the longest common prefix of "p and p(i,m)" }
//	static void EK( int m, char *p, int *a ){
//		int j = 0, k = 1;
//		while( j+1<m && p[j]==p[j+1] ) ++j;
//		a[0] = m;
//		if( m > 1 ) a[1] = j;
//		for(int i=2; i<m; i++){
//			int Len = k+a[k]-1, L = a[i-k];
//			if( L < Len-i+1 ) a[i] = L;
//			else{
//				j = max( 0, Len-i+1 );
//				while( i+j<m && p[i+j]==p[j] ) ++j;
//				a[i] = j; k = i;
//			}
//		}
//	}
//	// b[i] = { the longest common prefix of "p and t(i,n)" }
//	static void EK( int n, char *t, int m, char *p, int *b ){
//		int *a = new int[m];
//		EK( m, p, a );
//		int j = 0, k = 0;
//		while( j<n && j<m && p[j]==t[j] ) ++j;
//		b[0] = j;
//		for(int i=1; i<n; i++){
//			int Len = k+b[k]-1, L = a[i-k];
//			if( L < Len-i+1 ) b[i] = L;
//			else{
//				j = max( 0, Len-i+1 );
//				while( j<m && i+j<n && p[j]==t[i+j] ) ++j;
//				b[i] = j; k = i;
//			}
//		}
//		delete []a;
//	}
//	// judge whether t(i,n-1)(0<=i<n) is a palindrome, return ok[]
//	static void Palindrome( int n, char *t, bool *ok ){
//		char *s = new char[n];
//		for(int i=0; i<n; i++) s[i] = t[n-1-i];
//		int *b = new int[n];
//		EK( n, t, n, s, b );
//		memset( ok, false, sizeof(bool)*n );
//		for(int i=0; i<n; i++) if( b[i]==n-i ) ok[i] = true;
//		delete []s;
//		delete []b;
//	}
//	static __int64 Num( int ps, Node *p, int n, char *t, bool *ok ){
//		__int64 s = 0;
//		for(int i=0; i<n; i++){
//			int v = t[i]-'a';
//			ps = p[ps].ch[v];
//			if( ps == -1 ) break;
//			if( i<n-1 && ok[i+1] ) s += p[ps].t;
//		}
//		if( ps != -1 ) s += p[ps].t+p[ps].s;
//		return s;
//	}
//	static void ans(){
//		int n;
//		Node *p = new Node[2000000];
//		while( scanf("%d",&n)==1 ){
//			int *m = new int[n];
//			char **s = new char*[n];
//			bool *ok = new bool[n];
//			p[0].set( '$' );
//			for(int i=0, pn=0; i<n; i++){
//				scanf("%d",&m[i]);
//				s[i] = new char[m[i]+1];
//				scanf("%s",s[i]);
//				Palindrome( m[i], s[i], ok );
//				//for(int j=0; j<m; j++) printf("%d ",ok[j]); printf("\n");
//				Insert( 0, pn, p, m[i], s[i], ok );
//			}
//			//for(int i=0; i<n; i++) Insert( 0, pn, p, s[i] );
//			//Show( 0, p, 1 );
//			__int64 num = 0;
//			for(int i=0; i<n; i++){
//				for(int j=0; j<m[i]/2; j++) swap( s[i][j], s[i][m[i]-1-j] );
//				Palindrome( m[i], s[i], ok );
//				//for(int j=0; j<m; j++) printf("%d ",ok[j]); printf("\n");
//				num += Num( 0, p, m[i], s[i], ok );
//				//cout<<num<<endl;
//			}
//			printf("%I64d\n", num );
//			for(int i=0; i<n; i++) delete []s[i];
//			delete []s;
//			delete []m;
//			delete []ok;
//		}
//		delete []p;
//	}
//};
//
//int main(){
//	Trie::ans();
//	//Palindromes::ans();
//	/*int n; char *s; bool *ok;
//	srand((unsigned)time(NULL));
//	while( scanf("%d",&n)==1 ){
//		clock_t st = clock();
//		s = new char[n+1];
//		ok = new bool[n];
//		for(int i=0; i<n; i++){
//			s[i] = 'a'+rand()%26;
//		}
//		s[n] = '\0';
//		Palindromes::Palindrome( n, s, ok );
//		delete []ok;
//		delete []s;
//		clock_t ed = clock();
//		printf("%.4lf\n",(double)(ed-st)/CLOCKS_PER_SEC);
//		st = clock();
//		for(int i=0; i<10*n; i++) int j = i;
//		ed = clock();
//		printf("%.4lf\n",(double)(ed-st)/CLOCKS_PER_SEC);
//	}*/
//	return 0;
//}


//#include<iostream>
//using namespace std;
//
//class Trie{
//    struct Node{ int s[26], p; };
//public:
//    static void Init( int &ps, Node *P, int p ){
//        for(int i=0; i<26; ++i) P[ps].s[i] = -1;
//        P[ps++].p = p;
//    }
//    static void Insert( int &ps, Node *P, char *s ){
//        int w = 0, k = strlen(s);
//        for(int i=0; i<k; ++i){
//            int t = s[i]-'a';
//            if( P[w].s[t] == -1 ){
//                P[w].s[t] = ps;
//                Init( ps, P, w );
//            }
//            w = P[w].s[t];
//        }
//    }
//    static void Match( int ps, Node *P, int w, int m, char *s, int &num ){
//        if( w == m ){ ++num; return; }
//        if( s[w] != '(' ){
//            int t = s[w]-'a';
//            if( P[ps].s[t] != -1 ) Match( P[ps].s[t], P, w+1, m, s, num );
//        }
//        else{
//            int nw = ++w;
//            while( s[nw]!=')' ) ++nw;
//            while( w<nw ){
//                int t = s[w++]-'a';
//                if( P[ps].s[t] != -1 ) Match( P[ps].s[t], P, nw+1, m, s, num );
//            }
//        }
//    }
//    static void ans(){
//        int l, d, n;
//        Node *p = new Node[100008];
//        char s[400];
//        while( scanf("%d%d%d",&l,&d,&n)==3 ){
//            int ps = 0, t = 0;
//            Init( ps, p, -1 );
//            while( d-- ){
//                scanf("%s",s);
//                Insert( ps, p, s );
//            }
//            while( n-- ){
//                scanf("%s",s);
//                int num = 0;
//                Match( 0, p, 0, strlen(s), s, num );
//				printf("Case #%d: %d\n", ++t,num);
//            }
//        }
//        delete []p;
//    }
//};
//
//int main(){
//	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\input.in", "r", stdin );
//	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\acm.out", "w", stdout );
//    Trie::ans();
//    return 0;
//}


#include<iostream>
#include<time.h>
using namespace std;

int main(){
	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\input.in", "r", stdin );
	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\acm.out", "w", stdout );

    int tt, d[508][19];
    char c, s[508], t[20]={"welcome to code jam"};
    scanf("%d",&tt);
    getchar();
    for(int r=1; r<=tt; r++){
        int n = 0, num = 0;
        while( (c=getchar())!='\n' ) s[n++] = c;
        //memset( d[0], 0, sizeof(int)*20 );
        for(int i=0; i<n; i++){
            for(int j=0; j<19; j++) d[i][j] = 0;
			if( s[i]==t[0] ) d[i][0] = 1;
            for(int j=1; j<19; j++){
                d[i][j] = 0;
                if( s[i]!=t[j] ) continue;
                for(int k=i-1; k>=0; k--) d[i][j] += d[k][j-1];
                d[i][j] %= 10000;
            }
			//printf("%d\n",d[i][18]);
            num = (num+d[i][18])%10000;
        }
        printf("Case #%d: %04d\n",r,num);
    }
    return 0;
}
