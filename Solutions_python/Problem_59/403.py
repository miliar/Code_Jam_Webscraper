#!/usr/bin/env python2.6
"Module docstring"

from optparse import OptionParser
import sys


def do_job(in_file, out_file, verbose=False):
    "Do the work"
    if verbose:
        print "Start working with files: %s and %s" % (in_file, out_file)
    # test cases
    T = int(in_file.readline())
    for testcase in range(T):
        N, M = map(int, in_file.readline().split())
        tree = set()
        result = 0
        for _ in xrange(N):
            new_path = in_file.readline().lstrip('/').rstrip('\n').split('/')
            for i in xrange(1, len(new_path)+1):
                tree.add(tuple(new_path[:i]))
        if verbose:
            print tree
        for _ in xrange(M):
            new_path = in_file.readline().lstrip('/').rstrip('\n').split('/')
            for i in xrange(1, len(new_path)+1):
                new_dir = tuple(new_path[:i])
                if new_dir not in tree:
                    result += 1
                    tree.add(new_dir)
        if verbose:
            print tree



#        values = map(int, in_file.readline().split())
#        values = in_file.readline().rstrip('\n')
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print >> out_file, "Case #%d:" % (testcase + 1),
    print >> out_file, result

def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    usage = "%prog -V -t template | -r in_file [-w out_file]"
    parser = OptionParser(usage = usage)
    parser.add_option("-t", dest = "template",
            help = "template name for construct in file name as \
TEMPLATE.in")
    parser.add_option("-r", dest = "in_file",
            help = "input file or stdin if FILE is -")
    parser.add_option("-w", dest = "out_file",
            help = "output file or stdout if FILE is - (default case) or \
TEMPLATE.out (default if template is given)")
    parser.add_option("-V", "--verbose", dest = "verbose",
            action="store_true", default=False,
            help = "run as verbose mode")

    #I don't like args;)
    (options, _) = parser.parse_args(argv)
    if options.template and options.in_file:
        print "Options -t and -r are exclusive."
        parser.print_help()
        return 1
    if not options.in_file and not options.template:
        print "Must provide a filename or a template."
        parser.print_help()
        return(1)
    if options.template:
        options.in_file = ''.join((options.template, '.in'))
    if options.in_file == '-':
        in_file = sys.stdin
    else:
        try:
            in_file = open(options.in_file, 'r')
        except IOError:
            print "File, %s, does not exist." % options.in_file
            parser.print_help()
            return(1)
    if options.template and not options.out_file:
        options.out_file = ''.join((options.template, '.out'))
    if not options.out_file or options.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(options.out_file, 'w')
        except IOError:
            print "Problem opening file: %s" % options.out_file
            parser.print_help()

    sys.setrecursionlimit(2**31-1)
    do_job(in_file, out_file, options.verbose)
    return 0
if __name__ == '__main__':
    sys.exit(main())
