#include <iostream>
#include <cstdlib>
#include <ctime>
#include <math.h>
#define maxsize 10
using namespace std;
int main()
{
        srand((unsigned)time(0));
	int tests;
    long students, width, length;
    double studReach[maxsize];
    double posX[maxsize];
    double posY[maxsize];
    cin >> tests;
	for(int i = 1; i<=tests; i++){
	    cin >> students >> width >> length;
        for(int j = 0; j<students; j++){
            cin >> studReach[j];
            posX[j]=0;
            posY[j]=0;
        }
        restart:
        for(int j=0;j<students;j++){
            posX[j]=(rand()/double(RAND_MAX)*width);
            posY[j]=(rand()/double(RAND_MAX)*length);
            for(int k=0;k<j;k++){
                double distance=sqrt((posX[j]-posX[k])*(posX[j]-posX[k])+(posY[j]-posY[k])*(posY[j]-posY[k]));
                if(distance < studReach[j]+studReach[k]+0.1){
                    goto restart;
                }
            }
        }
        cout.precision(2);
        cout.setf(ios::fixed,ios::floatfield);
	    cout << "Case #"<<i<<": ";
        for(int j = 0; j<students; j++){
            cout << posX[j] << " " << posY[j] << " ";
        }
        cout << endl;
	}
}
