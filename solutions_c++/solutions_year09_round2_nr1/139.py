#include <cstdio>
#include <cstddef>
#include <cassert> 

#include <string>
#include <set>



class DTree {
        long double m_weight;
        
        std::string m_feature;
        
        DTree * m_left;
        
        DTree * m_right;
        

        DTree();
        DTree(const DTree &);
        DTree & operator =(const DTree &);
        
public:
        
        DTree(FILE * file) {
                char tmp[2];
                
                fscanf(file, "%1s", tmp);
                assert( tmp[0] == '(' );
                
                fscanf(file, "%Lf", &m_weight);
                
                fscanf(file, "%1s", tmp);
                ungetc(tmp[0], file);
                
                if( tmp[0] == ')' ) {
                        m_left = NULL;
                        m_right = NULL;
                } else {
                        char word[1024];
                        fscanf(file, "%1023s", word);
                        m_feature = word;
                        
                        m_left = new DTree(file);
                        m_right = new DTree(file);
                }
                
                fscanf(file, "%1s", tmp);
                assert( tmp[0] == ')' );
        }
        

        virtual ~DTree() {
                delete m_left;
                delete m_right;
        }
        
        
        long double process(const std::set<std::string> & animal) const {
                long double res = m_weight;
                
                if( animal.find(m_feature) != animal.end() ) {
                        if( m_left != NULL )
                                return m_weight * m_left->process(animal);
                        return m_weight;
                
                } else {
                        if( m_right != NULL )
                                return m_weight * m_right->process(animal);
                        return m_weight;
                }
        }
};

int main() {
        size_t T;
        scanf("%u", &T);
        
        for(size_t t = 0; t < T; ++t) {
                printf("Case #%u:\n", t + 1);
                        
                size_t L;
                scanf("%u", &L);
                DTree dtree(stdin);
                
                size_t A;
                scanf("%u", &A);
                
                for(size_t a = 0; a < A; ++a) {
                        std::set<std::string> animal;
                        
                        size_t N;
                        char word[1024];
                        
                        scanf("%1023s%u", word, &N);
                        
                        for(size_t n = 0; n < N; ++n) {
                                scanf("%1023s", word);
                                animal.insert(word);
                        }
                        
                        printf("%.7Lf\n", dtree.process(animal));
                }
        }
        
        return 0;
}