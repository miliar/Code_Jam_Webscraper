#include <list>
#include <algorithm>
#include <iostream>

struct combine {
    char spell;
    char result;
    combine *c_spell;
};

struct opposed {
    char spell;
    opposed *c_spell;
};

bool cmp_combine( combine *a, combine *b ) {return a->spell < b->spell; }
bool cmp_opposed( opposed *a, opposed *b ) {return a->spell < b->spell; }

using namespace std;

void print_invk(list<char> *invk, int num_case) {
    
    printf("Case #%d: [", num_case);
    
    if (!invk->empty()) {
        
        list<char>::iterator it = invk->begin();
        printf("%c", *it);
        
        it++;
        
        while (it != invk->end()) {
            printf(", %c", *it);
            it++;
        }
    }
    
    printf("]\n");
}

int main() {
    combine c_array[73];
    opposed o_array[57];
    
    list<combine*> combine_list;
    list<opposed*> opposed_list;
    list<char> invk;
    
    combine *c_find;
    opposed *o_find;
    
    c_find = new combine;
    o_find = new opposed;
    
    int num_combine, num_opposed, num_cases, num_spells, j, idx_c, idx_o;
    
    cin >> num_cases;
    
    for(int i=1; i<=num_cases; i++) {
        
        idx_c = idx_o = 0;
        
        cin >> num_combine;
        
        for(j=0; j<num_combine; j++) {
            combine *a, *b;
            
            a = &c_array[idx_c++];
            b = &c_array[idx_c++];
            
            cin >> a->spell;
            cin >> b->spell;
            cin >> a->result;
            b->result = a->result;
            
            a->c_spell = b;
            b->c_spell = a;
            
            combine_list.push_back(a);
            combine_list.push_back(b);
        }
        
        combine_list.sort(cmp_combine);
        
        cin >> num_opposed;
        
        for(j=0; j<num_opposed; j++) {
            opposed *a, *b;
            
            a = &o_array[idx_c++];
            b = &o_array[idx_c++];
            
            cin >> a->spell;
            cin >> b->spell;
            
            a->c_spell = b;
            b->c_spell = a;
            
            opposed_list.push_back(a);
            opposed_list.push_back(b);
        }
        
        opposed_list.sort(cmp_opposed);
        
        cin >> num_spells;
        
        for(j=0; j<num_spells; j++) {
            char spell;
            cin >> spell;
            
            invk.push_back(spell);
        }
        
        if(num_opposed == 0 && num_combine == 0 || num_spells == 0) {
            print_invk(&invk, i);
            combine_list.clear();
            opposed_list.clear();
            invk.clear();
            continue;
        }
        
        list<char>::iterator it;
        list<char>::iterator tmp;
        
        list<combine*>::iterator c_pos;
        list<opposed*>::iterator o_pos;
        
        for( it = invk.begin(); it != invk.end(); it++) {
            c_find->spell = o_find->spell = *it;
            
            o_pos = lower_bound(opposed_list.begin(), opposed_list.end(), o_find, cmp_opposed);
            
            if( (*o_pos)->spell == *it ) {
                tmp = it;
                
                do {
                    tmp--;
                    
                    if (*tmp == (*o_pos)->spell ) {
                        break;
                    }
                    
                    if (*tmp == (*o_pos)->c_spell->spell) {
                        tmp = it;
                        tmp++;
                        it = invk.erase(invk.begin(), tmp);
                        it--;
                        break;
                    }
                }while (tmp != invk.end());
            }
            
            c_pos = lower_bound(combine_list.begin(), combine_list.end(), c_find, cmp_combine);
            //printf("curr: %c  found: %c\n", *it, (*c_pos).spell);
            if( (*c_pos)->spell == *it ) {
                tmp = it;
                tmp++;
                //printf(" tmp: %c, cmp to: %c\n", *tmp, ((*c_pos).c_spell)->spell);
                if (tmp != invk.end() && (*tmp) == ((*c_pos)->c_spell)->spell) {
                    //printf(" erasing from: %c to %c\n", *it, *tmp);
                    tmp++;
                    it = invk.erase(it, tmp);
                    invk.insert(it, (*c_pos)->result);
                    it--;
                    //printf(" adding: %c\n", (*c_pos).result);
                    continue;
                }
            }
            
        }
        
        print_invk(&invk, i);
        
        combine_list.clear();
        opposed_list.clear();
        invk.clear();
    }
    
    return 0;
}