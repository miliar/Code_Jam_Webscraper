#include<stdio.h>
#include<vector>
using namespace std;
vector<int> visit;
int A,B,tmp[20];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("pc.txt","w",stdout);
	int T,cnt,ten,shift,ans,t;
	scanf(" %d",&T);
	for( int x = 1; x <= T; x++ ){
		scanf(" %d %d",&A,&B);
		ans = 0;
		for( int i = A; i <= B; i++ ){
            //change to array
			tmp[0] = i % 10;
			for( cnt = 1, ten = 10; i/ten > 0; ten*=10 )
				tmp[cnt++] = ( i / ten ) % 10;
			visit.clear();
			for( int j = 1; j < cnt; j++ ){
                //shift
				t = tmp[cnt-1];
				for( int k = cnt-1; k > 0; k-- )
				    tmp[k] = tmp[k-1];
				tmp[0] = t;
				//count shift
				if( tmp[cnt-1] == 0 )   continue;
				shift = tmp[cnt-1];
				for( int k = cnt-2; k >= 0; k-- )
                    shift = 10 * shift + tmp[k];
                bool see = false;
                for( int k = 0; k < visit.size(); k++ )
                    if( shift == visit[k] ) see = true;
                visit.push_back(shift);
                if( !see && shift <= B && shift > i )   ans++;
			}
		}
		printf("Case #%d: %d\n",x,ans);
	}
	return 0;
}
