#include <cstdio>

#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <math.h>

#include <algorithm>

#define INPUT_INT(inp) scanf("%d", &(inp));
#define INPUT_UINT(inp) scanf("%u", &(inp));
#define INPUT_LNG(inp) scanf("%ld", &(inp));
#define INPUT_DBL(inp) scanf("%f", &(inp));
#define INPUT_STR(inp) scanf("%s", inp);

#define OUTPUT_INT(i, val) printf("Case #%d: %d\n", (i), (val));
#define OUTPUT_UINT(i, val) printf("Case #%d: %u\n", (i), (val));
#define OUTPUT_LNG(i, val) printf("Case #%d: %ld\n",(i), (val));
#define OUTPUT_ULNG(i, val) printf("Case #%d: %lu\n",(i), (val));
#define OUTPUT_LNGLNG(i, val) printf("Case #%d: %lld\n",(i), (val));
#define OUTPUT_DBL(i, val) printf("Case #%d: %f\n", (i), (val));
#define OUTPUT_STR(i, str) printf("Case #%d: %s\n", (i), (str));

#define FOR(i, start, end) for(i = start; i < end; i++)
#define ROF(i, end, start) for(i = end - 1; i >= start; i--)

using namespace std;

// Declare globals here
static void solve(int);

// Utility Data structures
struct tree_node_s {
    uint8_t digit;
    map<uint8_t, tree_node_s*> children;
    struct tree_node_s *parent;
} root;

void delete_underlying_tree(tree_node_s *root)
{
    if (root != NULL) {
	map<uint8_t, tree_node_s*>::iterator it;
	for (it = root->children.begin(); it != root->children.end(); it++) {
	    delete_underlying_tree(it->second);
	    delete it->second;
	}
	root->children.clear();
    }
}
 
int add_to_tree(tree_node_s *root, uint32_t add_this_number, uint8_t num_digits)
{
    uint32_t divisor = (uint32_t)(pow10(num_digits - 1));
    uint32_t remainder = 0;
    tree_node_s *current_node = root;
    bool already_exists = true;

    while (divisor != 0) {
	
	uint8_t digit = (uint8_t) (add_this_number / divisor);
	if (current_node->children.count(digit) == 0) {
	
	    // digit not found. insert in tree.
	    already_exists = false;
	    tree_node_s *new_node = new tree_node_s;
	    new_node->digit = digit;
	    new_node->parent = current_node;
	    
	    current_node->children.insert(pair<uint8_t, tree_node_s*>(digit, new_node));
	    current_node = new_node;
	
	} else {

	    // digit found.
	    current_node = current_node->children.find(digit)->second;
	}
	
	add_this_number = add_this_number % divisor;
	divisor = divisor / 10;
    } 

    return already_exists;
}

uint8_t find_number_of_digits(uint32_t A)
{
    uint8_t num_digits = 0;
    while (A != 0) {
	num_digits += 1;
	A /= 10;
    }
    return num_digits;
}

uint64_t find_number_of_recycled(uint32_t X, uint32_t A, uint32_t B, uint8_t num_digits)
{
    uint32_t back, front, recycled;
    uint64_t num_recycled = 0;
    uint32_t divisor = 10;
    uint32_t anti_divisor = (uint32_t) (pow10(num_digits - 1));
    
    // Cook-up the tree
    root.digit = 0;
    root.parent = NULL;
    
    add_to_tree(&root, X, num_digits);
    
    while (divisor <= X) {
	
	back = X % divisor;

	if (back < (divisor / 10)) {
	    // this contains leading zeroes. Move on.
	    divisor = divisor * 10;
	    anti_divisor = anti_divisor / 10;
	    continue;
	}

	front = (uint32_t) (X / divisor);
	recycled = (back * anti_divisor) + front;

	if (recycled != X && recycled >= A && recycled <= B) {
	    bool already_exists = add_to_tree(&root, recycled, num_digits);
	    if (!already_exists) num_recycled++;
	}

	divisor = divisor * 10;
	anti_divisor = anti_divisor / 10;
    }

    // Delete tree
    delete_underlying_tree(&root);

    return num_recycled;
}

void solve(int testcase)
{
    // Declarations
    uint32_t A, B, i;
    uint64_t num_recycled = 0;

    // Scan Input
    INPUT_INT(A);
    INPUT_INT(B);

    uint8_t num_digits = find_number_of_digits(A);

    // Calculations
    FOR(i, A, B + 1) {
    	num_recycled += find_number_of_recycled(i, A, B, num_digits);
    }

    // Output
    OUTPUT_ULNG(testcase, (uint64_t)(num_recycled / 2));
    
    // Cleanup
}

int main()
{
    // Declarations
    int N = 0, testcase = 1;

    // Get number of cases
    INPUT_INT(N);

    while (N--) {
	solve(testcase++);
    }

    return 0;
}

