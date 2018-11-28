/*
 * File:   template.c
 * Author: rsalmeidafl
 *
 * Created on 26 de Julho de 2008, 23:32
 */

#include <stdio.h>
#include <stdlib.h>

const int OR = 0;
const int AND = 1;
const int LEAF = 2;

struct node {
    int kind;
    int value;
    int changeable;
};

int min(int a, int b) {
    return (a < b) ? a : b;
}

int process_tree(node *tree, int i, int target) {
    if (tree[i].kind == LEAF) {
        if (tree[i].value == target)
            return 0;
        else
            return -1;
    }
    else {
        int op1 = process_tree(tree, 2*i + 1, target);
        int op2 = process_tree(tree, 2*i + 2, target);

        if (target == 1 && tree[i].kind == AND || target == 0 && tree[i].kind == OR) {
            if (tree[i].changeable) {
                if (op1 == -1 && op2 == -1)
                    return -1;
                else if (op1 == -1)
                    return 1 + op2;
                else if (op2 == -1)
                    return 1 + op1;
                else
                    return min(1 + min(op1, op2), op1 + op2);
            }
            else {
                if (op1 == -1 || op2 == -1)
                    return -1;
                else
                    return op1 + op2;
            }
        }
        else if (target == 1 && tree[i].kind == OR || target == 0 && tree[i].kind == AND) {
            if (op1 == -1 && op2 == -1)
                return -1;
            else if (op1 == -1)
                return op2;
            else if (op2 == -1)
                return op1;
            else
                return min(op1, op2);
        }
    }
}

/*
 *
 */
int main(int argc, char** argv) {

    int number_of_test_cases;
    int current_test_case = 1;

    scanf("%d", &number_of_test_cases);

    while (current_test_case <= number_of_test_cases) {
        /* Input */
        node heap[10000] = {0};
        int heap_size;
        int root_val;
        
        scanf("%d", &heap_size);
        scanf("%d", &root_val);

        int i = 0;

        for (;i < (heap_size - 1)/2; ++i) {
            scanf("%d", &heap[i].kind);
            scanf("%d", &heap[i].changeable);
        }

        for (; i < heap_size; ++i) {
            heap[i].kind = LEAF;
            scanf("%d", &heap[i].value);
        }

        /* Computations */
        int number_of_gate_changes = process_tree(heap, 0, root_val);

        /* Output */
        if (number_of_gate_changes == -1)
            printf("Case #%d: IMPOSSIBLE\n", current_test_case);
        else
            printf("Case #%d: %d\n", current_test_case, number_of_gate_changes);

        /* Loop */
        ++current_test_case;
    }


    return (EXIT_SUCCESS);
}


