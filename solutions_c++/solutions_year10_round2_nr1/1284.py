#include <iostream>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <string>
#include <vector>
using namespace std;

map<string, int> mmp;
int N, M, id;
vector<int> t[100000+5];
vector<int> jlN[100+5], jlM[100+5];

void read(){
	int i, j, k;
	char str[1000+5];
	string tstr;
	scanf("%d%d", &N, &M);
	for( i=1; i<=N; ++i ){
		jlN[i].clear();
		jlN[i].push_back(0);
	}
	for( i=1; i<=M; ++i ){
		jlM[i].clear();
		jlM[i].push_back( 0 );
	}
	mmp.clear();
	id = 0;
	for( i=1; i<=N; ++i ){
		scanf("%s", str );
		tstr.clear();
		for( j=1; str[j]; ++j ){
			if( str[j]=='/' ){
				if( mmp.find(tstr)==mmp.end() ){
					mmp[tstr]=++id;
					jlN[i].push_back( id );
				}else
					jlN[i].push_back( mmp.find(tstr)->second );
				tstr.clear();
			}else{
				tstr +=str[j];
			}
		}
			if( mmp.find(tstr)==mmp.end() )
				mmp[tstr]=++id;
			jlN[i].push_back( mmp.find(tstr)->second );
		
	}

	for( i=1; i<=M; ++i ){
		scanf("%s", str );
		tstr.clear();
		for( j=1; str[j]; ++j ){
			if( str[j]=='/' ){
				if( mmp.find(tstr)==mmp.end() ){
					mmp[tstr]=++id;
					jlM[i].push_back( id );
				}else
					jlM[i].push_back( mmp.find(tstr)->second );
				tstr.clear();
			}else{
				tstr +=str[j];
			}
		}

		if( mmp.find(tstr)==mmp.end() ){
			mmp[tstr]=++id;
			jlM[i].push_back( id );
		}else
			jlM[i].push_back( mmp.find(tstr)->second );
	}

}

#define keyNum 200

struct trie {
    struct trieNode {
        trieNode * link[keyNum];

        trieNode() {
            memset(link, NULL, sizeof (link));
        }
    };
    trieNode* root;

    trie() {        root = new trieNode;    }
    void Insert(vector<int>, bool jia);
};


int ans;
void trie::Insert( vector<int> vi, bool jia ) {
    trieNode *current = root;
    int i = 1;
    while ( i<vi.size() ) {
		if (current->link[vi[i] ] == NULL){
            current->link[vi[i] ] = new trieNode;
			if( jia ) ans++;
		}
        current = current->link[vi[i]];
        i++;
    }
}

void solve(){
	int i, j; 
	ans = 0;
	trie a;
	for( i=1; i<=N; ++i ){
		a.Insert( jlN[i], 0 );
	}	

	for( j=1; j<=M; ++j ){
		a.Insert( jlM[j], 1 );
	}
	printf("%d\n", ans );
}

int main(){
	//freopen("d:\\in.txt", "r", stdin );
	//freopen("d:\\A-small-attempt2.in", "r", stdin );
	//freopen("d:\\A.out", "w", stdout );
	freopen("d:\\A-small-attempt3.in", "r", stdin );
	freopen("d:\\A.out", "w", stdout );
	int num_case;
	scanf("%d", &num_case );
	for( int i=1; i<=num_case; ++i ){
		if( i==49 )
			int zp = 2;
		printf("Case #%d: ", i );
		read();
		solve();
	}
	return 0;
}
