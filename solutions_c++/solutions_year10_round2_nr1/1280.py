//#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>

#include <vector>

using namespace std;

/*
1 <= T <= 42
2 <= N_B <= 3
*/

int T, N, M;

#define T_MAX 100
#define N_MAX 9
#define M_MAX 10

FILE *fin;


void Solve(int numTestCase) {
    //int i, j;
}

#define STRLEN_MAX 102


typedef struct StructPath {
    char str[STRLEN_MAX];
    //int numChild;
    vector<struct StructPath> child;
} Path;

Path fsRoot;

int IndexSubdir(Path &p, char *subDir) {
    int i;
    for (i = 0; i < p.child.size(); i++) {
        Path &childUnused = p.child[i];
        if (strcmp(p.child[i].str, subDir) == 0)
            return i;
    }
    return -1;
}

void ReadData() {
    int i, j;
    char str[STRLEN_MAX + 1];
    int numMkDirs;

    fscanf(fin, "%d\n", &T);
    assert(T >= 1 && T <= T_MAX);

    strcpy(fsRoot.str, "/");
    //fsRoot.numChild = 0;
    for (i = 0; i < T; i++) {
        numMkDirs = 0;

        fgets(str, STRLEN_MAX, fin);
        sscanf(str, "%d %d", &N, &M);
        //fscanf(fin, "%d", &T);

        for (j = 0; j < N; j++) {
            fgets(str, STRLEN_MAX, fin);
            str[strlen(str) - 1] = 0;
            assert(str[0] == '/'); 

            char *sAux = &str[1];
            char *sAuxOld;

            Path *crtDir = &fsRoot;
            for (;;) {
                sAuxOld = sAux;
                for (; *sAux != '/'; sAux++)
                    if (*sAux == 0)
                        break;

                char subDirStr[STRLEN_MAX + 1];
                strncpy(subDirStr, sAuxOld, sAux - sAuxOld);
                subDirStr[sAux - sAuxOld] = 0;
                int pos = IndexSubdir(*crtDir, subDirStr);
                if (pos == -1)
                //mkdir
                {
                    Path c;
                    strcpy(c.str, subDirStr);
                    crtDir->child.push_back(c);
                    Path &childUnused = crtDir->child[0];
                    //crtDir = &c;
                    crtDir = &(crtDir->child[crtDir->child.size() - 1]);
                }
                else {
                    crtDir = &(crtDir->child[pos]);
                }


                if (*sAux == 0)
                    break;
                sAux++;
            }
        }

        for (j = 0; j < M; j++) {
            fgets(str, STRLEN_MAX, fin);
            str[strlen(str) - 1] = 0;
            assert(str[0] == '/'); 

            char *sAux = &str[1];
            char *sAuxOld;

            
            Path *crtDir = &fsRoot;
            for (;;) {
                sAuxOld = sAux;
                for (; *sAux != '/'; sAux++)
                    if (*sAux == 0)
                        break;
                char subDirStr[STRLEN_MAX + 1];
                strncpy(subDirStr, sAuxOld, sAux - sAuxOld);
                subDirStr[sAux - sAuxOld] = 0;
                int pos = IndexSubdir(*crtDir, subDirStr);
                if (pos == -1)
                //mkdir
                {
                    Path c;
                    strcpy(c.str, subDirStr);
                    crtDir->child.push_back(c);
                    Path &childUnused = crtDir->child[0];
                    //crtDir = &c;
                    crtDir = &(crtDir->child[crtDir->child.size() - 1]);
                    numMkDirs++;
                }
                else {
                    crtDir = &(crtDir->child[pos]);
                }

                if (*sAux == 0)
                    break;
                sAux++;
            }
        }

        printf("Case #%d: %d\n", i + 1, numMkDirs);
        fflush(stdout);

        fsRoot.child.clear();
    }
}

int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
    /*
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.in", "rt", stdin);
    freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large.out", "wt", stdout);
    */
    //freopen("A-large-practice.in", "rt", stdin);
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large-practice.out", "wt", stdout);

    //freopen("A.in", "rt", stdin);
    //freopen("A_orig.in", "rt", stdin);
    //freopen("A-small-attempt2.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("A.out", "wt", stdout);

    fin = stdin;
    ReadData();

    fclose(fin);

    return 0;
}
