#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <cassert>
using namespace std;

const long MAX_N = 1000;
long R, N, k;
long long res_notes[MAX_N+1];
int next_head[MAX_N+1];
long long res;

struct Group {
    long val;
    int id;
    Group(long val_, int id_) : val(val_), id(id_) { }
    void show() { cout << "# " << id << " " << val; }
};

queue<Group *> *perm_queues[MAX_N+1];


int main(int argc, char **argv)
{
    int NC;
    int case_no;
    int cur_head;
    long i, x, r;
    Group *g;
    
    if (argc < 2) {
        cerr << "Please, provide input file." << endl;
        return 1;
    }

    ifstream in(argv[1]);
    ofstream out(argc < 3 ? "th_park.out" : argv[2]);
    in >> NC;

    for (case_no = 1; case_no <= NC; case_no++) {
        in >> R >> k >> N;
        queue<Group *> q;
        for (i = 1; i <= N; i++) {
            in >> x;
            q.push(new Group(x, i));
        }

        // make permutation queues
        for (i = 1; i <= N; i++) {
            perm_queues[i] = new queue<Group *>(q);
            g = q.front();
            q.pop();
            q.push(g);
        }
        /*
        while(!q.empty()) {
            g = q.front();
            q.pop();
            g->show(); cout << endl;
        }
        */
        // init 
        res = 0;
        fill(res_notes, res_notes+MAX_N+1, -1);
        fill(next_head, next_head+MAX_N+1, -1);
        cur_head = 1;
        
        for (r = 1; r <= R; r++) {
            long passengers = 0;
            
            if (next_head[cur_head] != -1) { 
                // i have memoization
                assert(res_notes[cur_head] != -1);
                passengers = res_notes[cur_head];
                
            } else {
                // have to do some calculations
                queue<Group *> *p_q = perm_queues[cur_head];
                while (true) {
                    g = p_q->front();
                    // have troubles with cheaters?
                    if (passengers != 0 && g->id == cur_head)
                        break;
                    if (passengers+g->val <= k)  {
                        passengers += g->val;
                        p_q->pop();
                        p_q->push(g);
                    } else 
                        break;
                }
                assert(passengers != 0);

                // take notes of what have just seen
                next_head[cur_head] = p_q->front()->id;
                res_notes[cur_head] = passengers;
            } // end calculations
            res += passengers;
            cur_head = next_head[cur_head];
        }
        
        out << "Case #" << case_no << ": " << res << endl;
        // clear queues
        while (!q.empty()) {
            g = q.front();
            q.pop();
            delete g;
        }       
        for (i = 1; i <= N; i++) {
            delete perm_queues[i];
            perm_queues[i] = NULL;
        }
        
    }

    in.close();
    out.close();
    return 0;
}
