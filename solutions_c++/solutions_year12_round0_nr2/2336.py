#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;
void parseFile(){
    ifstream file;
    file.open("B-large.in",ios::in);
    ofstream o_file;
    o_file.open("output.txt",ios::out);
    int t, count = 1,num, surp, best, t_point, iter=0;
    //int *t_points;
    int s_count=0, ave, nums[0], max, a_count=0;
    file>>t;
    while(count <=t) {
        //cout<<"#"<<count<<"\n";
        file>>num;
        //cout<<num<<" ";
        file>>surp;
        //cout<<surp<<" ";
        file>>best;
        //cout<<best<<" ";
        o_file<<"Case #"<<count<<": ";
        //t_points = new int[num];
        while(iter++ < num) {
            //file>>t_points[iter++];
            file>>t_point;
            //cout<<t_point<<" ";
            ave = t_point/3;
            //assuming surprising are with diff 2 from ave*3 
            // by definition of bad this is the only possibility
            // expand to surp like 7 7 9
            if(best == 0) {
                a_count++;
                continue;
            }
            if(t_point == 0 ) {
                continue;
            }
            // 7 7 9 7 8
            if(s_count != surp && t_point%3 == 2 && (ave+1 == best -1) ){ 
                max = ave + 2;
                s_count ++;
            }
            // case of 6 7 8
            else if(s_count != surp && t_point%3 == 0 && (ave == best - 1)){
                max = ave + 1;
                s_count ++;
            }
            // all surp accountedor surp not needed  expand to 7 8 8
            else if(t_point%3 == 2) {
                max = ave + 1;
            }
            // all surp accounted exp to 7 7 8
            else if(t_point%3 == 1){
                max = ave + 1;
            }
            // expand to 7 7 7
            else {
                max = ave;
            }
            
            if(max >= best)
                    a_count++;
        }
        //cout<<"\n";
//        cout<<"Found Surprising "<<s_count<<"\n";
//        cout<<"Answer "<<a_count<<"\n";
//        cout<<"#######################################\n";
        o_file<<a_count<<"\n";
        iter = 0;
        a_count = 0;
        s_count = 0;
        count++;
    }
}
int main(int argc, char** argv) {
    parseFile();
    return 0;
}
