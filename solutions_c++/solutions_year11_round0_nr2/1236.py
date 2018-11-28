#include <stdio.h>
#include <vector>

using namespace std;

typedef vector<char> Str;

struct Com
{
	char c[2];
	char t;

	bool match(char a, char b){
		return (a == c[0] && b == c[1])
			|| (a == c[1] && b == c[0])
			;
	}

	bool apply(Str& s, int pos){
		if( s.size() < pos + 2 ) return false;

		// 基本、先頭と末端にしか反応しない
		if( /*pos != 0 &&*/ pos != s.size() - 2 ) return false;

		if( match( s[pos], s[pos+1] ) ){
			s.erase( s.begin() + pos );
			s.erase( s.begin() + pos );
			s.insert( s.begin() + pos, t );
			return true;
		}
		return false;
	}
};

struct Opp
{
	char c[2];

	bool match(char a, char b){
		return (a == c[0] && b == c[1])
			|| (a == c[1] && b == c[0])
			;
	}

	bool apply(Str& s, int pos){

		if( s.size() < pos + 2 ) return false;

		// 先頭から最短マッチする場所を探す
		char f = s[pos];
		for(int i = pos+1;i < s.size();++i){
			if( match(f, s[i]) ){
				s.erase( s.begin() + pos, s.begin() + i + 1 );
				return true;
			}
		}

		return false;
	}
};

typedef vector<Com> VCom;
typedef vector<Opp> VOpp;

int main(void)
{
	int T = 0;
	scanf("%d",&T);

	VCom com;
	VOpp opp;

	for(int round = 0;round < T;++round){

		int C = 0;
		int D = 0;
		int N = 0;

		com.clear();
		opp.clear();

		scanf("%d",&C);
		for(int i = 0;i < C;++i){
			Com c;
			scanf(" %c%c%c", &(c.c[0]), &(c.c[1]), &(c.t));
			com.push_back(c);
		}

		scanf("%d",&D);
		for(int i = 0;i < D;++i){
			Opp o;
			scanf(" %c%c", &(o.c[0]), &(o.c[1]));
			opp.push_back(o);
		}

		Str org;
		char dc;
		scanf("%d",&N);
		scanf("%c",&dc);
		for(int i = 0;i < N;++i){
			scanf("%c",&dc);
			org.push_back(dc);
		}

		//for(int i = 0;i < com.size();++i){
		//	printf("%c%c%c ",com[i].c[0],com[i].c[1],com[i].t);
		//}
		//for(int i = 0;i < opp.size();++i){
		//	printf("%c%c ",opp[i].c[0],opp[i].c[1]);
		//}
		//for(int i = 0;i < s.size();++i){
		//	printf("%c",s[i]);
		//}
		//printf("\n");

		// えーと、
		// まず、 combine を最優先で両端にかける。
		// その後、いずれかの opposed が発動しないか確認。
		// 基本、この繰り返しでいける。

		Str s;

		// 一文字ずつ invoke !
		for(int tpos = 0;tpos < org.size();++tpos){

			s.push_back( org[tpos] );
			if(s.size() < 2)continue;

			bool isC = false;
			bool isO = false;

			// できあがった呪文を逐一チェック

				// 末尾くっつけられる？
				// combine
				for(int i = 0;i < com.size();++i){
					if( s.size() > 1 && com[i].apply(s,s.size()-2) ){
					}
				}
				
				for(int pos = 0;s.size() > 0 && pos < s.size()-1;++pos){
					// opposed
					for(int i = 0;i < opp.size();++i){
						if( opp[i].apply(s,pos) ){
							pos = 0;

							s.clear();

							//for(int i = 0;i < s.size();++i){
							//	printf("%c",s[i]);
							//}
							//printf("\n");
							isO = true;
						}
					}
					if(isO){ pos = 0; isO = false; }
				}

		}

		// 完成披露
		printf("Case #%d: [",round + 1);
		for(int i = 0;i < s.size();++i){
			if(i != 0) printf(" ");
			printf("%c",s[i]);
			if(i + 1 != s.size()) printf(",");
		}
		printf("]\n");
	}

	return 0;
}