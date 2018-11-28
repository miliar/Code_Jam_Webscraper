#include <cstdio>
#include <cstdlib>
#include <string>
#include <bitset>
#include <vector>
#include <cmath>

#define pb push_back

using namespace std;

int t, r, mdz_x1, mdz_x2, mdz_y1, mdz_y2;
bitset<1000> bs[2][1000];
vector<int> v_x1, v_x2, v_y1, v_y2;

int main()
{
    int i, j, k, tag, up, down, ans;
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
       	v_x1.clear();
       	v_x2.clear();
       	v_y1.clear();
       	v_y2.clear();

        scanf("%d", &r);
        while (r--) {
            scanf("%d %d %d %d", &mdz_x1, &mdz_y1, &mdz_x2, &mdz_y2);
            v_x1.pb(mdz_x1);
            v_y1.pb(mdz_y1);
            v_x2.pb(mdz_x2);
            v_y2.pb(mdz_y2);
        }
        
        int min_x1 = v_x1[0];
        int max_x1 = v_x1[0];
        int min_y1 = v_y1[0];
        int max_y1 = v_y1[0];
        int min_x2 = v_x2[0];
        int max_x2 = v_x2[0];
        int min_y2 = v_y2[0];
        int max_y2 = v_y2[0];
        for (j = 1; j < v_x1.size(); j++) {
            min_x1 = min(min_x1, v_x1[j]);
            max_x1 = max(max_x1, v_x1[j]);
            min_y1 = min(min_y1, v_y1[j]);
            max_y1 = max(max_y1, v_y1[j]);
            min_x2 = min(min_x2, v_x2[j]);
            max_x2 = max(max_x2, v_x2[j]);
            min_y2 = min(min_y2, v_y2[j]);
            max_y2 = max(max_y2, v_y2[j]);
        }
        
        int min_x = min(min_x1, min_x2);
        int max_x = max(max_x1, max_x2);
        int min_y = min(min_y1, min_y2);
        int max_y = max(max_y1, max_y2);
        
        max_x -= min_x;
        max_y -= min_y;
        for (j = 0; j < v_x1.size(); j++) {
            v_x1[j] -= min_x;
            v_y1[j] -= min_y;
            v_x2[j] -= min_x;
            v_y2[j] -= min_y;
        }
        
        up = 0;
        down = 1;
        for (j = 0; j <= max_x; j++)
        	for (k = 0; k <= max_y; k++)
        		bs[0][j][k] = bs[1][j][k] = 0;
                
        for (r = 0; r < v_x1.size(); r++) 
            for (j = v_x1[r]; j <= v_x2[r]; j++)
            	for (k = v_y1[r]; k <= v_y2[r]; k++)
            		bs[up][j][k] = 1;
        
        tag = 1;
        ans = 0;
        while (tag) {
            tag = 0;
            ans++;
            
            for (j = 0; j <= max_x; j++)
            	for (k = 0; k <= max_y; k++)
            		bs[down][j][k] = 0;
           	for (j = 1; j <= max_x; j++)
           		for (k = 1; k <= max_y; k++)
           			if (bs[up][j - 1][k] && bs[up][j][k - 1]) {
           				bs[down][j][k] = 1;
           				tag = 1;
          			} else if (bs[up][j][k] &&
             			(bs[up][j - 1][k] || bs[up][j][k - 1])) {
         				bs[down][j][k] = 1;
         				tag = 1;
         			}
     		for (j = 1; j <= max_x; j++)
     			if (bs[up][j][0] && bs[up][j - 1][0]) {
     			    bs[down][j][0] = 1;
     			    tag = 1;
     			}    
    		for (k = 1; k <= max_y; k++)
    			if (bs[up][0][k] && bs[up][0][k - 1]) {
    			    bs[down][0][k] = 1;
    			    tag = 1;
    			}    

         	/*	
     		for (j = 0; j < 10; j++) {
     		    for (k = 0; k < 10; k++)
     		    	printf("%d", bs[down][j][k] ? 1 : 0);
    		    printf("\n");
     		}
       		printf("\n");    
       		*/
     		
     		up = down;
     		down = 1 - up;
        }    
        
        printf("Case #%d: %d\n", i + 1, ans);
    }    
    
    return (0);
}

    
