#include <cstdio>
#include <algorithm>
#include <set>


using namespace std;



int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		
        int N,L,H; scanf("%d %d %d\n", &N, &L, &H);
        
        set<int> notes;
        
        for (int i=0; i<(H-L+1); i++) notes.insert(L+i);

        
        for (int i=0; i<N; i++){
            
            int noteB;scanf("%d",&noteB);
            
            set<int>::iterator it=notes.begin();
            
            while(it != notes.end()){

                std::set<int>::iterator current = it++;
                int noteA = *current;
                
                if((noteA % noteB >0) && (noteB % noteA >0)){
                    notes.erase(current);
                }
           }
            
           
        }
        
        if (notes.empty()){
            printf("NO\n",N);
        
        }else{
            set<int>::const_iterator it = notes.begin();
            printf("%d\n",*it);
        }
        
    }
            
	return 0;
}
