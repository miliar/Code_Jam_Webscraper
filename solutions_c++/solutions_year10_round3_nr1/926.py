#include<cstdio>
#include<QtCore/QMap>
#include<QtCore/QList>
//Qt can be obtained under the LGPL at qt.nokia.com

int main()
{
    int T,N; //per spec
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        scanf("%d", &N);

        QMap<int, int> wires;//autosorted by key
        for(int n=0; n<N; n++){
            int a,b;
            scanf("%d %d\n", &a, &b);
            wires.insert(a,b);
        }
        int c = 0;
        QList<int> A;
        for(QMap<int,int>::const_iterator iter = wires.constBegin(); iter!=wires.constEnd(); iter++)
            A << iter.key();
        for(int i=0; i<A.count(); i++)
            for(int j=i+1; j<A.count(); j++)
                if(wires[A[i]] > wires[A[j]])
                    c++;

        printf("Case #%d: %d\n", t, c);
    }
    return 0;
}

