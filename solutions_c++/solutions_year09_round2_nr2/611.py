#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

const int max_size = 20 + 5;

vector <int> num;
char data[max_size];

int main()
{
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    
    int nCase;
    scanf("%d", &nCase);
    
    for (int t=0; t<nCase; t++){
        scanf ("%s", data);
        
        
        num.clear();
        
        for (int i=0; i<strlen(data); i++)
            num.push_back(data[i] - '0');
            
            
        printf ("Case #%d: ", t + 1);
        
        if (next_permutation(num.begin(), num.end())) {
            for (int i = 0; i < num.size(); ++i)
                printf ("%d", num[i]);
            printf ("\n");
        }
        else {
            sort(num.begin(), num.end());
            int i = 0;
            while (num[i] == 0 && i < num.size()) i++;
            
            if (i != 0) {
                num[0] = num[i];
                num[i] = 0;
            }
            
            printf("%d", num[0]); printf("0");
            for (i=1; i < num.size(); i++) {
                printf ("%d", num[i]);
            }
            printf ("\n");
        }
    }
    
    return 0;
}
