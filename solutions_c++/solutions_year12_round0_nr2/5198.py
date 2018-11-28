// google code jam 002.cpp : メイン プロジェクト ファイルです。

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#define DATA_SET_SIZE 10


#include <vector>

using namespace std;

#define NUM_OF_SET 3

typedef struct Set{
    int data[NUM_OF_SET];
    bool surprising_;

    Set(int input[3], bool sur){
        for(int i=0;i<3;i++){
            data[i] = input[i];
        }
        surprising_ = sur;
    }

    bool Get(int output[3]){
        for(int i=0;i<3;i++){
            output[i] = data[i];
        }
        return surprising_;
    }

    bool Evaluate(int val){
        for(int i=0;i<NUM_OF_SET;i++){
            if(val <= data[i]){
                return true;
            }
        }
    }

    //bool IsSurprising(){
    //    for(
    //}
};

typedef class Set1{
private:
    int target_;
    vector<Set> pattern_;

public:
    Set1(int input){ target_ = input;}
    ~Set1(){;}

    void CreatePattern(){
        pattern_.clear();

        int ave = target_ / NUM_OF_SET;
        int diff = target_ - ave * NUM_OF_SET;
        printf("target:%d ave:%d diff:%d\n", target_, ave, diff);

        for(int k=ave-2;k<=ave;k++){ // 1番小さい値
            if(k<0){
                continue;
            }

            for(int l=k;l<=k+2;l++){ // 2番目に小さい値
                int m = target_ - k - l;
                if(m - k > 2 || l > m){
                    continue;
                }
                int d[NUM_OF_SET] = {k, l, m};
                printf("%d %d %d\n", d[0], d[1], d[2]);

                Set set(d, m-k==2 ? true : false);
                pattern_.push_back(set);
            }
        }
    }
    //void CreatePattern_(){
    //    pattern_.clear();

    //    int ave = target_ / NUM_OF_SET;
    //    int diff = target_ - ave * NUM_OF_SET;
    //    printf("target:%d ave:%d diff:%d\n", target_, ave, diff);

    //    for(int k=ave-2;k<=ave;k++){ // 1番小さい値
    //        if(k<0){
    //            continue;
    //        }
    //        int m = k + 2; //一番大きい値
    //        int l = target_ - k - m; // 真ん中の値

    //        if(m < l || l < k){
    //            continue;
    //        }
    //        int d[NUM_OF_SET] = {k, l, m};
    //        printf("%d %d %d\n", d[0], d[1], d[2]);

    //        pattern_.push_back(d);
    //    }
    //}

    int Size(){
        return pattern_.size();
    }

    bool GetPattern(int i, int d[3]){
        if(i >= pattern_.size()){
            return false;
        }
        return pattern_[i].Get(d);
    }

    bool Evaluate(int i, int val){
        if(i >= pattern_.size()){
            return false;
        }
        return pattern_[i].Evaluate(val);
    }
};

typedef class Param{
public:
    int N_;
    int S_;
    int p_;
    int data_[DATA_SET_SIZE];

private:
    vector<Set1> pattern_;
    int size_;

public:
    Param(){
        N_ = 0;
        S_ = 0;
        p_ = 0;
        for(int i=0;i<DATA_SET_SIZE;i++){
            data_[i] = 0;
        }

        size_ = 0;
    }
    ~Param(){
        ;
    }

    void Reset(){
        printf("%s -->\n", __FUNCTION__);
        pattern_.clear();

        int num = N_;
        for(int i=0;i<num;i++){
            printf("%d ", i);
            Set1 set(data_[i]);
            pattern_.push_back(set);
        }
        printf(" = %d\n", pattern_.size());
        printf("%s <--\n", __FUNCTION__);
    }

    void CreatePattern(){
        printf("%s -->\n", __FUNCTION__);

        int num = pattern_.size();
        for(int i=0;i<num;i++){
            printf("%d ", i);
            pattern_[i].CreatePattern();
        }

        size_ = 1;
        num = pattern_.size();
        for(int i=0;i<num;i++){
            size_ *= pattern_[i].Size();
        }
        printf("\n");
        printf("%s <--\n", __FUNCTION__);
    }

    int Size(){
        return size_;
    }

    void GetData(int index, int d[3]){
    }

    void ShowData(){
        printf("N_ : %d S_ : %d p_ : %d |", N_, S_, p_);
        for(int j=0;j<N_;j++){
            printf(" %2d,", data_[j]);
        }
        printf("\n");
    }

    int Calc(){
        int num = pattern_.size();
        int max_point = 0;
        for(int i=0;i<size_;i++){
            printf("[%d]:", i);
            int m = 1;
            for(int j=0;j<num-1;j++){
                m *= pattern_[j].Size();
            }
            int temp = 0;
            int index = 0;
            int point_count = 0;
            int combination_count = 0;
            for(int j=0;j<num;j++){
                index = (i - temp) / m;
                if(j != num-1){
                    //printf("(%d << %d %d %d", index, (i - temp), m, temp);
                    temp += (i - temp) - i % m;
                    m /= pattern_[j].Size();
                }else{
                    //printf("(%d << %d %d %d", index, (i - temp), m, temp);
                }

                printf("%d", index);
                int d[NUM_OF_SET] = {0};
                combination_count += pattern_[num - 1 -j].GetPattern(index, d);
                printf("(");
                for(int k=0;k<NUM_OF_SET;k++){
                    printf(",%d", d[k]);
                }
                printf("):%d, ", pattern_[num - 1 -j].Evaluate(index, p_));
                point_count += pattern_[num - 1 -j].Evaluate(index, p_);
            }
            printf(" ===> \%d] in %d ...", point_count, combination_count);
            if(combination_count != S_){
                printf("(%d!=%d)\n", combination_count, S_);
            }else{
                printf("OK!\n");
                if(max_point < point_count){
                    max_point = point_count;
                }
            }
        }
        printf("Case #o: %d\n", max_point);
        return max_point;
    }
};

using namespace System;

int main(array<System::String ^> ^args)
{
    //ifstream ifs("input_1.txt");
    ifstream ifs("input.txt");
    string buf;
    int line_count = 0;
    int num_of_data = 0;
    Param* data;
    while(ifs && getline(ifs, buf)){
        if(line_count == 0){
            istringstream is(buf);
            is >> num_of_data;
            cout << "num_of_data:" << num_of_data << endl;

            data = new Param[num_of_data];
        }else{
            istringstream is(buf);

            int index = line_count - 1;
            is >> data[index].N_;
            is >> data[index].S_;
            is >> data[index].p_;
            for(int i=0;i<data[index].N_;i++){
                is >> data[index].data_[i];
            }
        }
        cout << buf << endl;
        line_count++;
    }

    printf("-----------------------------------------------------------\n");
    printf("- parsed data ---------------------------------------------\n");
    for(int i=0;i<num_of_data;i++){
        data[i].ShowData();
    }
    printf("-----------------------------------------------------------\n");

    // main operation

    int* result = new int[num_of_data];
    for(int i=0;i<num_of_data;i++){
        data[i].Reset();
        data[i].CreatePattern();
        result[i] = data[i].Calc();
    }


    printf("\n");
    printf("\n");
    ofstream ofs("output.txt");
    for(int i=0;i<num_of_data;i++){
        printf("Case #%d: %d\n", i+1, result[i]);
        ofs << "Case #" << i+1 << ": " << result[i] << endl;
    }

    // finalize
    delete[] data;

    char s[10];
    gets(s);
    return 0;
}
