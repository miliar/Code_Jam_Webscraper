#include <iostream>
#include <algorithm>
#include <string>
#include <cstdlib>

using namespace std;
namespace
{
}

class Robot
{
    int m_position;
    int m_time;
public:
    Robot() : m_position(1), m_time(0) {}
    int MoveAndPush(int p){
        int t=abs(p-m_position)+1; // +1: ボタンを押す分
        m_time+=t;
        m_position=p;
        return m_time;
    }
    void SetGlobalTime(int t){
        m_time=t;
    }
};

class Task
{
public:
    Robot *m_robot;
    int m_position;

    Task() : m_robot(NULL), m_position(0) {}
    void Initialize(Robot *r, int p) {
        m_robot=r;
        m_position=p;
    }
    int Wait(){
        return m_robot->MoveAndPush(m_position);
    }
};

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        Robot orange, blue;
        int N;
        cin >> N;
        Task *tasks=new Task[N];
        for(int j=0; j<N; j++){
            char name;
            int position;
            cin >> name >> position;
            switch(name){
            case 'O':
                tasks[j].Initialize(&orange, position);
                break;
            case 'B':
                tasks[j].Initialize(&blue, position);
                break;
            default:
                cerr << "Invalid Robot Name" << endl;
                exit(-1);
            }
        }
        int globalTime=0;
        for(int j=0; j<N; j++){
            int t=tasks[j].Wait();
            if(globalTime<t){
                //cerr << "(" << j << ") global<t: " << globalTime << ", " << t << endl;
                globalTime=t;
            }else{
                //cerr << "(" << j << ") global>=t: " << globalTime << ", " << t << endl;
                globalTime++;
                tasks[j].m_robot->SetGlobalTime(globalTime);
            }
        }
        cout << "Case #" << (i+1) << ": " << globalTime << endl;

        delete tasks;
    }
    return 0;
}
