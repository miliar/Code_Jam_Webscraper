#include <iostream>
#include <fstream>

using namespace std;
bool intersect(int A1, int B1, int A2, int B2){
    if (A1 < A2 && B1 < B2)
        return false;
    if (A1 > A2 && B1 > B2)
        return false;
    return true;
}
int solve(int* A, int* B, int N){
    int inter_count = 0;
    for (int i=0;i < N;i++){
        for (int j=0;j < N;j++){
            if (i == j)
                continue;
            if (intersect(A[i], B[i], A[j], B[j]))
                inter_count++;
        }
    }
    return inter_count/2;
}
int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in >> T;
    int N;
    int A[1000];
    int B[1000];
    for (int i=0;i < T;i++){
        in >> N;
        for (int j=0;j < N;j++)
            in >> A[j] >> B[j];
        out << "Case #" << i+1 << ": " << solve(A, B, N) << endl;
    }
    in.close();
    out.close();
}
