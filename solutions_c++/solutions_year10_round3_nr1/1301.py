#include <cstdio>

struct Line {
    unsigned left;
    unsigned right;

    Line(unsigned left_, unsigned right_) : left(left_), right(right_) {}
    Line() : left(0), right(0) {}

    void init(unsigned left_, unsigned right_) { left = left_; right = right_; }
};

bool isIntersect(Line& line1, Line& line2) {
    if(line1.left == line2.left) {
        return true;
    } else if(line1.left > line2.left) {
        return (line1.right <= line2.right);
    } else if(line1.left < line2.left) {
        return (line1.right >= line2.right);
    }
}

const unsigned MAX_LINES = 1200;
const unsigned MAX_TESTS = 20;

int main() {
    Line input[MAX_LINES];

    FILE *fin=fopen("C:/A-large.in","r");
	FILE *fout= fopen("C:/A-large-0.txt","w");

	unsigned tests;
	fscanf(fin, "%u", &tests);

    unsigned count_int[MAX_TESTS];
    for(unsigned t = 0; t < tests; ++t) {
        unsigned num_lines;
        fscanf(fin, "%u", &num_lines);

        unsigned l, r;
        for(unsigned i = 0; i < num_lines; ++i) {
            fscanf(fin, "%u %u", &l, &r);
            input[i].init(l,r);
        }

        for(unsigned i = 0; i < num_lines - 1; ++i) {
            for(unsigned j = i + 1; j < num_lines; ++j) {
                if(isIntersect(input[i],input[j])) ++count_int[t];
            }
        }
    }

    for(unsigned i = 0; i < tests; ++i) {
        fprintf(fout, "Case #%u: %u\n", i+1, count_int[i]);
    }
}
