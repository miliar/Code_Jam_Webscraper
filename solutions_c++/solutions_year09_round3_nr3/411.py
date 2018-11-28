#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

int main()
{
    FILE *in,*out;
    int casen,T,i,j,k,p,n,min,count;
    set<int>::iterator iter,iter2;
    
    in = fopen("in.txt","r");
    out = fopen("out.txt","w");
    
    fscanf(in,"%d\n",&T);
    for (casen = 1; casen <= T; casen++) {
        fscanf(in,"%d %d", &p, &n);
        
        set<int> room;
        vector<int> Q(n);
        
        room.insert(0);
        room.insert(p+1);
        
        for (i=0; i<n; i++)
            fscanf(in,"%d", &Q[i]);
        
        min = 5000;
        do {
            count = 0;
            set<int> r = room;
            for(i=0; i<n; i++) {
                iter = iter2 = r.upper_bound(Q[i]);
                iter --;
                
                count += *iter2 - *(iter) - 2;
                
                r.insert(Q[i]);
            }
            
            if (count < min)
                min = count;
        
        } while (next_permutation(Q.begin(), Q.end()));
        fprintf(out,"Case #%d: %d\n", casen, min);
    }
    
    fclose(in);
    fclose(out);
}
