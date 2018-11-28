#include <string>
#include <iostream>

struct info {
    int last_value;
    int last_time;
};

using namespace std;

int main() {
    int curr, req, total, num_inputs, num_cases, i, j;
    char type;
    info o, b, *c;
    
    cin >> num_cases;
    
    for (i=1; i<=num_cases; i++) {
        
        cin >> num_inputs;
        
        total = 0;
        o.last_time = b.last_time = 0;
        o.last_value = b.last_value = 1;
        
        if (num_inputs == 0) {
            printf("Case #%d: 0\n", i);
            continue;
        }
        
        for (j=0; j<num_inputs; j++) {
            
            cin >> type;
            cin >> curr;
            
            c = (type == 'O') ? &o : &b;
            
            req = abs( curr - c->last_value ) - (total - c->last_time);
            
            //printf("%d, %d, %d\n", req, c->last_time, abs( curr - c->last_value ));
            
            if (req < 0) {
                req = 0;
            }
            
            req++;
            total += req;
            //printf("total: %d\n", total);
            c->last_time = total;
            c->last_value = curr;
        }
        
        printf("Case #%d: %d\n", i, total);
    }
    
    return 0;
}
