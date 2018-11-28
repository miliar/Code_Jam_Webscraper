#include <iostream>
#include <sstream>
#include "simpio.h"
#include "vector.h"
#include <math.h>
#include "/Users/leungtimothy/Desktop/StanfordCPPLib/error.h"
using namespace std;
int indexMax(Vector<Vector<int> > list);
int main(){
    ifstream fin;
    ofstream fout;
    fin.open("/Users/leungtimothy/Desktop/problem2.txt");
    fout.open("/Users/leungtimothy/Desktop/problem2.result.txt");
    
    Vector<Vector<int> > list;
    Vector<int> tuple;
    int testNumber;
    int N;
    int S;
    int P;
    
    int totalNum;
    fin >> totalNum;
    cout << totalNum;
    for (int num = 0; num < totalNum; num++) {
        int i,j,k;
        
        
        int count = 0;
        fin >> N;
        fin >> S;
        fin >> P;
        for (int x = 0; x < N ; x++) {
            i = 0;
            j = 0;
            k = 0;
            fin >> testNumber;
            while (true) {
                if (i + j + k == testNumber) {
                    break;
                }
                k++;
                if (i + j + k == testNumber) {
                    break;
                }
                j++;
                if (i + j + k == testNumber) {
                    break;
                }
                i++;
            }
            tuple.add(i);
            tuple.add(j);
            tuple.add(k);
            tuple.add(testNumber);
            list.add(tuple);
            tuple.clear();
        }
        
        foreach(Vector<int> tuple in list)
            cout << tuple[0] << tuple[1] << tuple[2] <<tuple[3] << endl;
        
        

        Vector<int> delIndex;
        delIndex.clear();
        cout << "list.size()" << list.size() << endl;
        for (int x = 0;  x < list.size(); x++) {
            cout << "number X " << x <<endl;
            if (list[x][2]>=P) {
                count++;
                cout << "removeAt x " << x << endl;
                delIndex.add(x);
            }
        }
        for (int i = delIndex.size()-1; i>=0; i--) {
            list.removeAt(delIndex[i]);
        }
        cout << "First count" << count;
        int index;
        
        
        if (list.size()>0) {
        //if we have surprise
        for (int x = 0; x < S; x++) {
            if (list.size() ==0) {
                break;
            }
            cout << " index" << index << list.size() << endl;
            index = indexMax(list);
            
            cout << list[index][3] << endl;
            if (list[index][3]<2 ||list[index][3] == 4 ||list[index][3] == 7 ||list[index][3] == 10 ||list[index][3] == 13 ||list[index][3] == 16 ||list[index][3] ==  19 ||list[index][3] == 22 ||list[index][3] == 25 ||list[index][3] == 28)
                break;
            if (list[index][2]+1>=P) {
                count++;
                list.removeAt(index);
            }
        }
        }
        list.clear();
        
        cout << "Case #" << num +1 << ": " << count << endl;
        fout << "Case #" << num +1 << ": " << count << endl;
    }
    fin.close();
    fout.close();
    return 0;
}

int indexMax(Vector<Vector<int> > list){
    int max = list[0][3];
    int index = 0;
    if (list.size()==1) {
        return 0;
    }
    for (int i = 1; i < list.size(); i ++) {
        if (list[i][3]>= max) {
            max = list[i][3];
            index = i;
        }
            
    }
    return index;
}