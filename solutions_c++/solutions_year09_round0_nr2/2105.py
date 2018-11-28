#include <stdio.h>
#include <vector>
#include <set>
#include <string>
//#include <libgen.h>
#include <iostream>

using namespace std;

typedef vector< vector<int> > Terr;
vector<Terr> allIn;

class ReadCases
{
private:
    FILE *fp_;

    bool init(const char *name)
    {
        fp_ = fopen(name, "r");
        if (!fp_)
        {
            cerr << "Could not open file: " << name <<'\n';
            return false;
        }
    }

public:
    ReadCases(const char *name)
    {
        init(name);
    }

    ~ReadCases()
    {
        if(fp_)
            fclose(fp_);
    }

    int readAllCases( )
    {
        // TEST CASE COUNT
        char line[1025];
        if (!fgets(line, sizeof line, fp_))
        {
            cerr << "nothign found in the file\n";
            return -1;
        }
        int N;
        sscanf(line, "%d", &N);
        // END

        // EACH TERRAIN
        for(int i =0;i<N;++i) 
        {
            // H W
            if (!fgets(line, sizeof line, fp_))
            {
                cerr << "H W NOT found\n";
                return -1;
            }
            int H=0,W=0;
            sscanf(line, "%d %d", &H, &W);

            Terr terr;
            for(int j=0;j<H;++j)
            {
                // ROW in H
                if (!fgets(line, sizeof line, fp_))
                {
                    cerr << "ROW NOT found\n";
                    return -1;
                }

                vector<int> row;
                int begin =0, numlen=0,wsl=0;
                for(int k=0;k<W;++k)
                {
                    wsl = strspn(line+begin, " \t");
                    begin+=wsl;
                    numlen = strspn(line+begin, "0123456789");
                    string s(line+begin, line+begin+numlen);
                    begin+=numlen;
                    row.push_back(atoi(s.c_str()));
                }
                terr.push_back(row);
            }
            allIn.push_back(terr);
        }

        return N;
    }
};

int DONTKNO = -1;
int SINK = -2;
int lowestCell(const Terr &t, int i, int j)
{
    int A=t[i][j];
    int cell=DONTKNO;

    // N
    if (i-1>=0 && A>t[i-1][j])
    {
        A=t[i-1][j];
        cell = (i-1)*t[0].size() + j;
    }

    // W
    if (j-1>=0 && A>t[i][j-1])
    {
        A=t[i][j-1];
        cell = i*t[0].size() + j-1;
    }

    // E
    if (j+1<t[0].size() && A>t[i][j+1])
    {
        A=t[i][j+1];
        cell = (i)*t[0].size() + j+1;
    }

    // S
    if (i+1<t.size() && A>t[i+1][j])
    {
        A=t[i+1][j];
        cell = (i+1)*t[0].size() + j;
    }

    if (cell == DONTKNO)
        return SINK;

    return cell;
}

int calcBasin(const Terr &t, Terr &v, int i, int j)
{
    int cell = lowestCell(t, i, j);
    if (cell == SINK)  // i,j is the SINK
    {
        return SINK;
    }

    int ni=cell/t[0].size();
    int nj=cell%t[0].size();
    if (v[ni][nj] == DONTKNO) 
    {
        v[ni][nj]=calcBasin(t,v,ni,nj);
    }

    int ret;
    if (v[ni][nj] == SINK)
        ret=cell;
    else
        ret=v[ni][nj];
    return ret;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cerr << "usage: a.out <file>\n";
        exit(0);
    }

    ReadCases r(argv[1]);
    r.readAllCases( );
    

    // EACH TERR
//     for(int i=0;i<allIn.size();++i)
//     {
//         printf("TERR: %d\n", i+1);
//         for(int k=0;k<allIn[i].size();++k) // EACH ROW
//         {    
//             int j=0;
//             for(;j<allIn[i][k].size();++j)
//             {
//                 printf("%d ",allIn[i][k][j]);
//             }
//             printf("\n");
//         }
// //        cout << "Case #" << i+1 << ": " << match << endl;
//     }
    
    for(int i=0;i<allIn.size();++i)
    {
        Terr &terr = allIn[i];
        Terr val, bt;

        vector<int> row(terr[0].size(), DONTKNO);
        for(int k=0;k<terr.size();++k) // EACH ROW
        {    
            val.push_back(row);
        }
        bt=val;
        for(int k=0;k<terr.size();++k) // EACH ROW
        {    
            int j=0;
            for(;j<terr[k].size();++j)
            {
                if (val[k][j] != DONTKNO) continue;

                int cell = calcBasin(terr, val, k,j);
                val[k][j] = cell;
            }
        }

        char sc='a';
        for(int k=0;k<allIn[i].size();++k) // EACH ROW
        {    
            int j=0;
            for(;j<allIn[i][k].size();++j)
            {
                if (bt[k][j] != DONTKNO) continue;

                if (val[k][j] == SINK)
                {
                    val[k][j] = sc++;
                    bt[k][j] = 1;
                }
                else
                {
                    int sink = val[k][j];
                    int ni = sink/val[k].size();
                    int nj = sink%val[k].size();

                    if (bt[ni][nj] == DONTKNO)
                    {
                        val[ni][nj]=val[k][j]= sc++;
                        bt[ni][nj]=1;
                    }
                    else
                    {
                        val[k][j]=val[ni][nj];
                    }

                    bt[k][j] = 1;
                }
            }
        }

        cout << "Case #" << i+1 << ":\n";
        for(int k=0;k<allIn[i].size();++k) // EACH ROW
        {    
            int j=0;
            for(;j<allIn[i][k].size();++j)
            {
                printf("%c ",(char)val[k][j]);
            }
            printf("\n");
        }

    }

    return 0;
}
