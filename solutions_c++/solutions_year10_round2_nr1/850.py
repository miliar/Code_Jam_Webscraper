#include<cstdio>
#include<cstdlib>
#include<QtCore/QSet>
#include<QtCore/QByteArray>
//Qt libs are LGPL and available at qt.nokia.com

int main(int argc, char* argv[]){
    int T,N,M; //as per spec
    scanf("%d\n", &T);
    for(int t=0; t<T; t++){
        scanf("%d %d\n", &N, &M);
        int c = 0;
        char* input = (char*)malloc(101*sizeof(char));
        QByteArray dir;
        QSet <QByteArray> dirs;
        dirs << QByteArray("/");
        dirs << QByteArray("");//root dir without trailing slash
        for(int n=0; n<N; n++){
            scanf("%s\n", input);
            dirs << QByteArray(input);
        }
        for(int m=0; m<M; m++){
            scanf("%s\n", input);
            dir = QByteArray(input);
            while(!dirs.contains(dir)){
                dirs << dir;
                c++;
                dir.truncate(dir.lastIndexOf("/")); //Check parent dir
            }
        }
        printf("Case #%d: %d\n", t+1, c);
    }
    return 0;
}
