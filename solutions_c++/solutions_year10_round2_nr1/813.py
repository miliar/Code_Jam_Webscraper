#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

struct tree {
    char name[105];
    struct tree * subs[10005];
    int numsubs;
};

struct tree thetree={};


int createcost( char * path ) {
    int count=0;
    char name[100];
    struct tree * mytree = &thetree;
    while (*path!='\0'&&*path!='\n') {
        int i=0;
        path++;
        while (*path!='/' && *path!='\0'&&*path!='\n') {
            name[i]=*path;
            path++;
            i++;
        }
        name[i]='\0';
        int j;
        for (j=0;j<mytree->numsubs;j++) {
            if (strcmp(mytree->subs[j]->name, name)==0) break;
        }
        if (j==mytree->numsubs) {
            count++;
            mytree->subs[mytree->numsubs]=(struct tree *)calloc(sizeof(struct tree),1);
            strcpy( mytree->subs[mytree->numsubs]->name, name );
            mytree->numsubs++;
        }
        mytree = mytree->subs[j];
    }
    return count;
}    
    

int main () {
    
    int numCases, kase;
    
    scanf("%d", &numCases );
    
    for (kase=1; kase<=numCases; kase++) {
        
        int n, m, count=0;
        char path[105];
        
        scanf("%d %d", &n, &m );
        
        for (int i=0; i<n; i++) {
            scanf("%s", path);
            (void) createcost( path );
        }
        
        for (int i=0; i<m; i++) {
            scanf("%s", path);
            count += createcost( path );
        }
        
        
        printf("Case #%d: %d\n", kase, count);
        
        for (int i=0;i<thetree.numsubs;i++) free(thetree.subs[i]);
        thetree.numsubs=0;
    }
    
    
    return 0;
    
}
