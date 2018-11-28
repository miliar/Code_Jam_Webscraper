#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

typedef struct {
    char name[128];
    int old;
} folder;

static int cmp(const void *p1, const void *p2){
    return strcmp(((folder *)p1)->name, ((folder *)p2)->name);
}

int main(){
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        int N, M;
        
        folder folders[256];
        char temp[128];
        
        //cin >> N >> M;
        //cout << "N " << N << "  M " << M << endl;
        
        scanf("%d %d", &N, &M);
        cin.getline(temp, 128); //skip
        for (int i = 0; i < N; i++){
            //gets(folders[i].name);
            cin.getline(folders[i].name, 128);
            //scanf("%s", folders[i].name);
            //cout << folders[i].name << endl;
            folders[i].old = 1;
        }
        for (int i = 0; i < M; i++){
            //gets(folders[N+i].name);
            cin.getline(folders[N+i].name, 128);
            folders[N+i].old = 0;
            for (int j = 0; j < N; j++)
                if (strcmp(folders[N+i].name, folders[j].name) == 0){
                    --i;
                    --M;
                    break;
                }
        }
                
        qsort(folders, N + M, sizeof(folder), cmp);
        
        //for (int i = 0; i < N+M; i++)
        //    cout << folders[i].name << endl;

        
        const char *current;
        current = "/";
        int res = 0;
        //cout << N << "   " << M << endl;
        for (int i = 0; i < M+N; i++){
            //cout << i << ": " << current << endl;
            //cout << current << " VS " << folders[i].name << " "  << folders[i].old << endl;
            if (folders[i].old){
                //nothing to do
            } else {
                //search first different char between current and folders[i].name
                int j;
                for (j = 0; ; j++)
                    if (current[j] != folders[i].name[j])
                        break;
                
                ++res;
                //count all '/' after this position
                for ( j = j+1; folders[i].name[j] != '\0'; j++)
                    if (folders[i].name[j] == '/')
                        ++res;
            }
            current = folders[i].name;
            //cout << "res = " << res << endl;
        }
        //cout << current << endl;
        cout << "Case #" << t+1 << ": " << res << endl;
    }
    return 0;
}
