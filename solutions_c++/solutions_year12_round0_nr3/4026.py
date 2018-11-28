#include <QtCore>

#include <gmpxx.h>
typedef mpz_class bigint;

char was[2000001] = {0};
int L, R;

int getNext(int x)
{
    int a,b=x;
    do {
        a = b % 10;
        b /= 10;
    } while(a==0 && b);
    while(x/=10)
        a*=10;
    return a+b;
}

int main()
{
    QFile file_in("C-large.in"), file_out("output.txt");
    if(!file_in.open(QFile::ReadOnly) || !file_out.open(QFile::WriteOnly))
        return EXIT_FAILURE;

    QTextStream fin(&file_in);
    //QTextStream fout(stdout);
    QTextStream fout(&file_out);

    int N;
    fin >> N;
    for(int Ni=0; Ni<N; ++Ni) {
        bigint res=0;
        fin >> L >> R;
        memset(was,0,sizeof was);
        for(int i=L; i<=R; ++i) {
            int cur=i,count=0;
            while(cur>2000000 || was[cur]==0) {
                if(L<=cur && cur<=R) {
                    ++count;
                    was[cur]=1;
                }
                cur=getNext(cur);
            }
            res += count*(count-1)/2;
        }
        fout << QString("Case #%1: ").arg(Ni+1) << QString::fromStdString(res.get_str());
        endl(fout);
    }

    file_in.close();
    file_out.close();
    return EXIT_SUCCESS;
}
