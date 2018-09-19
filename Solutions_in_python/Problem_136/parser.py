import sys

def parse(schema):
    ''' The schema is represented as a list, with each entry in the list
    corresponding to a line or group of lines in the input.
    Each list is a group containing three possible things:
        <tuple>     : the empty tuple () represents a line that contains an
                      'int' that specifies the number of lines in the subgroup
        <function>  : a unary function to transform that line
        <list>      : denotes a subgroup that will be repeated starting
                      from that line. An empty list defaults as [str], returning
                      the line as a string.

    Example: [(), [(), float, [lambda x: x.split()]]]
    This is the expected line format of the file:
        num_tests
            num_subtests
            some_float
                split_line
                split_line
                ...
            ...
    '''
    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    return grouper(lines, list(schema))

def grouper(lines, schema):
    ''' Parse schema by consuming lines'''
    if () not in schema:
        my_lines = [lines.pop(0) for _ in range(len(schema))]
        result = [x[0](x[1]) for x in zip(schema, my_lines)]
        return result[0] if len(result) == 1 else result
    index = schema.index(())
    count = int(lines[index])
    schema[index] = int
    sub_schema = schema.pop()
    if len(sub_schema) == 0: sub_schema = [str]
    my_lines = [lines.pop(0) for i in range(len(schema))]
    level = [x[0](x[1]) for x in zip(schema, my_lines)]
    cases = [grouper(lines, sub_schema[:]) for _ in range(count)]
    return level + [cases]
