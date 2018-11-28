#include <fstream>
#include <string>
#include <vector>

using namespace std;

short validate(string query, char w)
{
    short code=0;
    for(long i=0; i<query.size() && !code; i++)
        if(query[i]==w)
            code=1;
    return code;
}
int main()
{
    ifstream f;
    f.open("A-large.in");
    ofstream g;
    g.open("A-large.out");

    int L,D,N;
    f>>L>>D>>N;

    vector <string> words(5010);
    vector <short> valid(5010, 1);
    string query, buff;
    long sum;
    char x;



    getline(f, buff);

    for(int i=0; i<D; i++)
        getline(f, words[i]);



    for(int i=1; i<=N; i++)
    {

        for(int z=0; z<D; z++) valid[z]=1;

        for(int j=0; j<L; j++)
        {
            query="";
            if(f.peek()=='(')
            {
                f.get();
                while(f.peek()!=')')
                {
                    f.get(x);
                    query+=x;
                }
                f.get();
            }
            else
            {
                f.get(x);
                query=x;
            }

        if(f.peek()=='\n') f.get();

        for(int chk=0; chk<D; chk++)
            if(valid[chk]==1)
                if(!validate(query, words[chk][j]))
                    valid[chk]=0;


        }

        sum=0;
        for(int z=0; z<D; z++)
        {
            sum+=valid[z];

        }

        g<<"Case #"<<i<<": "<<sum<<endl;
    }


    f.close();
    g.close();

    return 0;
}
