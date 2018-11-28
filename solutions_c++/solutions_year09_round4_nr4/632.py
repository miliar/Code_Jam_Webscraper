#include<iostream.h>
#include<math.h>
using namespace std;

int i,j,k,N,C,c;
double x[3], y[3], r[3], answer;

double dist(int i,int j)
{
    return sqrt( (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) );
}

double getans(int i, int j)
{
    double answer = dist(i,j) + r[i] + r[j];
    if( 2*r[i] > answer)
        answer = 2*r[i];
    if( 2*r[j] > answer)
        answer = 2*r[j];
    return answer;
}

int main()
{
    cin>>C;
    for(c=1; c<=C; c++)
    {
        cin>>N;
        for(i=0; i<N; i++)
        {
            cin>>x[i]>>y[i]>>r[i];
        }
        
        double answer;
        if(N==1)
        {
            answer = 2*r[0];
        }
        else if(N==2)
        {
             answer = (r[0]>r[1])?r[0]:r[1];
             answer = 2*answer;
        }
        else
        {
            answer = getans(0,1);
            if(r[2] > answer)
                answer = r[2];
            cerr<<answer<<endl;
            double answer2 = getans(0,2);
            if(r[1] > answer2)
                answer2 = r[1];
            if(answer2 < answer)
                answer = answer2;
                cerr<<answer<<' '<<answer2<<endl;
            answer2 = getans(1,2);
            if(r[0] > answer2)
                answer2 = r[0];
            if(answer2 < answer)
                answer = answer2;
    cerr<<answer<<' '<<answer2<<endl;            
        }
        printf("Case #%d: %.6f\n", c, answer/2);
//        cout<<"Case #"<<c<<": "<< answer  <<endl//;
    }
}
