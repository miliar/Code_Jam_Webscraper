import unittest


def get(file_handle):
    return file_handle.readline().strip()


def examples(sample, create_example):
    with open("./data/{sample}.in".format(sample=sample), "r") as practice_file:
        example_count = int(get(practice_file))

        for i in range(0, example_count):
            example = create_example(practice_file)

            yield (example, i+1,)


test = unittest.TestCase("__init__")
